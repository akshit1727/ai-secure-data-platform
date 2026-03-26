import { useState } from "react";

function App() {
  const [input, setInput] = useState("");
  const [result, setResult] = useState(null);

  const analyze = async () => {
    const res = await fetch("http://127.0.0.1:8000/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ content: input }),
    });

    const data = await res.json();
    setResult(data);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>AI Log Analyzer 🔍</h1>

      <textarea
        rows="10"
        cols="60"
        placeholder="Paste logs here..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />

      <br /><br />

      <button onClick={analyze}>Analyze</button>

      {result && (
        <div>
          <h2>Risk Level: {result.risk_level}</h2>
          <h3>Insights:</h3>
          <ul>
            {result.insights.map((i, index) => (
              <li key={index}>{i}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;