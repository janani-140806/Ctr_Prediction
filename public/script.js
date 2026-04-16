const ctrForm = document.getElementById("ctrForm");
const predictBtn = document.getElementById("predictBtn");
const resultBox = document.getElementById("resultBox");

function showResult(message, isSuccess = true) {
  resultBox.classList.remove("hidden", "success", "error");
  resultBox.classList.add(isSuccess ? "success" : "error");
  resultBox.textContent = message;
}

ctrForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const payload = {
    age: Number(document.getElementById("age").value),
    gender: document.getElementById("gender").value,
    device: document.getElementById("device").value,
    category: document.getElementById("category").value,
    time: document.getElementById("time").value,
  };

  try {
    predictBtn.disabled = true;
    predictBtn.textContent = "Predicting...";

    const response = await fetch("http://localhost:3000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    const data = await response.json();

    if (!response.ok || !data.success) {
      throw new Error(data.message || "Prediction failed.");
    }

    showResult(`Predicted CTR: ${data.ctr}%`, true);
  } catch (error) {
    showResult(error.message || "Something went wrong.", false);
  } finally {
    predictBtn.disabled = false;
    predictBtn.textContent = "Predict CTR";
  }
});
