import { useEffect, useState } from 'react';
import axios from 'axios';
import html2pdf from 'html2pdf.js';

interface ScanHistoryItem {
  target: string;
  timestamp: string;
  summary: string;
}

function App() {
  const [url, setUrl] = useState('');
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [darkMode, setDarkMode] = useState(false);
  const [history, setHistory] = useState<ScanHistoryItem[]>([]);

  useEffect(() => {
    const saved = localStorage.getItem('osint-scan-history');
    if (saved) {
      setHistory(JSON.parse(saved));
    }
  }, []);

  useEffect(() => {
    localStorage.setItem('osint-scan-history', JSON.stringify(history));
  }, [history]);

  const handleScan = async () => {
    if (!url) return alert('Please enter a domain');
    setLoading(true);
    try {
      const response = await axios.post('http://localhost:8000/scan', { target: url });
      setData(response.data);
      console.log("Gemini Summary:", data.summary);


      const summaryText =
        response.data.summary?.candidates?.[0]?.content?.parts?.[0]?.text || '';

      const newEntry: ScanHistoryItem = {
        target: url,
        timestamp: new Date().toLocaleString(),
        summary: summaryText.slice(0, 300) + '...',
      };
      setHistory([newEntry, ...history]);
    } catch (err) {
      alert('Error scanning domain');
    }
    setLoading(false);
  };

  const exportPDF = () => {
    const content = document.getElementById('report-content');
    if (!content) return;
    html2pdf().from(content).save(`${data?.target}_report.pdf`);
  };

  return (
    <div className={`min-h-screen px-4 py-6 ${darkMode ? 'dark bg-gray-900 text-white' : 'bg-white text-black'}`}>
      <div className="max-w-4xl mx-auto space-y-6">
        {/* Header */}
        <div className="flex justify-between items-center">
          <h1 className="text-2xl font-bold">🛡 OSINT Recon Bot</h1>
          <button
            onClick={() => setDarkMode(!darkMode)}
            className="text-sm px-3 py-1 border rounded"
          >
            {darkMode ? '☀️ Light Mode' : '🌙 Dark Mode'}
          </button>
        </div>

        {/* Input */}
        <div className="flex gap-2">
          <input
            type="text"
            placeholder="Enter domain (e.g., handmadejoy.co.in)"
            className="w-full p-2 border rounded text-black"
            value={url}
            onChange={(e: React.ChangeEvent<HTMLInputElement>) => setUrl(e.target.value)}
          />
          <button
            onClick={handleScan}
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
            disabled={loading}
          >
            {loading ? 'Scanning...' : 'Scan'}
          </button>
        </div>

        {/* Report Section */}
        {data && (
          <>
            <div className="flex justify-end">
              <button
                onClick={exportPDF}
                className="bg-green-600 text-white px-4 py-1 rounded hover:bg-green-700"
              >
                📄 Export as PDF
              </button>
            </div>

            <div id="report-content" className="space-y-6">
              {/* Gemini Summary */}
              <div className="p-4 border rounded bg-gray-100 dark:bg-gray-800">
                <h2 className="text-lg font-semibold mb-2">Gemini Summary</h2>
                <pre className="whitespace-pre-wrap text-sm">
                  {data.summary?.candidates?.[0]?.content?.parts?.[0]?.text}
                </pre>
              </div>

              {/* Raw Output */}
              <div className="p-4 border rounded bg-gray-100 dark:bg-gray-800">
                <h2 className="text-lg font-semibold mb-2">Raw OSINT Output</h2>
                <pre className="text-xs whitespace-pre-wrap break-words">
                  {JSON.stringify(data.osint, null, 2).replace(
                    /(CVE-\d{4}-\d{4,7})/g,
                    (match) =>
                      `🔗 https://cve.mitre.org/cgi-bin/cvename.cgi?name=${match}`
                  )}
                </pre>
              </div>
            </div>
          </>
        )}

        {/* History */}
        {history.length > 0 && (
          <div className="p-4 border rounded bg-gray-50 dark:bg-gray-900">
            <h2 className="text-lg font-semibold mb-2">🔁 Scan History</h2>
            <ul className="list-disc ml-6 space-y-2 text-sm">
              {history.map((item, index) => (
                <li key={index}>
                  <strong>{item.target}</strong> — {item.timestamp}
                  <div className="text-gray-500 dark:text-gray-400">
                    {item.summary}
                  </div>
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
