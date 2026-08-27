document.getElementById("calculate").addEventListener("click", async () => {
  const a = document.getElementById("a").value;
  const b = document.getElementById("b").value;
  const operation = document.getElementById("operation").value;
  const resultEl = document.getElementById("result");

  resultEl.textContent = "...";

  try {
    const response = await fetch("/api/calculate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ a, b, operation }),
    });
    const data = await response.json();

    if (!response.ok) {
      resultEl.textContent = data.error || "Error";
      return;
    }

    resultEl.textContent = data.result;
  } catch (err) {
    resultEl.textContent = "Network error";
  }
});
