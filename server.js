/**
 * CTR Prediction System - Backend Server
 * Tech stack: Node.js, Express, MongoDB (Mongoose)
 */

const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
const path = require("path");

const Prediction = require("./models/Prediction");

const app = express();
const PORT = 3000;
const MONGO_URI = "mongodb://127.0.0.1:27017/ctrDB";

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, "public")));

/**
 * Simple rule-based CTR prediction logic.
 * Returns a percentage value between 5 and 95.
 */
function predictCTR({ age, gender, device, category, time }) {
  let score = 0.25; // baseline = 25%

  // Age impact
  if (age >= 18 && age <= 24) score += 0.16;
  else if (age <= 34) score += 0.11;
  else if (age <= 44) score += 0.06;
  else score += 0.02;

  // Gender impact (dummy weighting)
  if (gender === "Female") score += 0.05;
  else score += 0.03;

  // Device impact
  if (device === "Mobile") score += 0.12;
  else score += 0.07;

  // Category impact
  if (category === "Tech") score += 0.09;
  else if (category === "Fashion") score += 0.07;
  else if (category === "Food") score += 0.05;

  // Time of day impact
  if (time === "Evening") score += 0.08;
  else score += 0.04;

  // Keep in realistic range (5% to 95%)
  const bounded = Math.max(0.05, Math.min(0.95, score));
  return Number((bounded * 100).toFixed(2));
}

/**
 * POST /predict
 * Accepts user data and returns predicted CTR.
 * Also stores each request + prediction in MongoDB.
 */
app.post("/predict", async (req, res) => {
  try {
    const { age, gender, device, category, time } = req.body;

    // Basic validation
    if (
      age === undefined ||
      !gender ||
      !device ||
      !category ||
      !time
    ) {
      return res.status(400).json({
        success: false,
        message: "Please provide all required fields.",
      });
    }

    const parsedAge = Number(age);
    if (Number.isNaN(parsedAge) || parsedAge < 1 || parsedAge > 120) {
      return res.status(400).json({
        success: false,
        message: "Age must be a valid number between 1 and 120.",
      });
    }

    const ctr = predictCTR({
      age: parsedAge,
      gender,
      device,
      category,
      time,
    });

    const predictionDoc = new Prediction({
      age: parsedAge,
      gender,
      device,
      category,
      time,
      ctr,
    });

    if (mongoose.connection.readyState === 1) {
      await predictionDoc.save();
    }

    return res.json({
      success: true,
      ctr,
      message: "CTR predicted and saved successfully.",
    });
  } catch (error) {
    return res.status(500).json({
      success: false,
      message: "Internal server error.",
      error: error.message,
    });
  }
});

/**
 * Connect to MongoDB and start server
 */
async function startServer() {
  try {
    await mongoose.connect(MONGO_URI);
    console.log("Connected to MongoDB: ctrDB");
  } catch (error) {
    console.error("MongoDB connection failed (predictions won't be saved):", error.message);
  }

  app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
  });
}

startServer();
