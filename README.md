# 🔵 BlueTrack: The Ultimate Obstacle (or Smurf) Locator! 🚀

Welcome to **BlueTrack**! Ever wanted your computer to have eyes? Specifically, eyes that are *obsessed* with the color blue? Well, you've come to the right place. 

This project isn't just a script; it's your first step into the world of Computer Vision, wrapped in a fun, interactive package. Whether you're tracking a blue pen, a blue toy, or your favorite blue mug, BlueTrack has got your back!

## ✨ What's the Magic?

*   **🎯 Real-Time Detection:** Spot blue objects faster than you can say "OpenCV".
*   **✍️ Ghost Trails:** It doesn't just see you; it remembers where you've been. It draws a cool red trail (last 100 points) following your blue object's movement.
*   **📏 Precision Tracking:** Get live X and Y coordinates displayed right on your screen. You're basically a NASA engineer in your local now.
*   **🖼️ Smart Filtering:** Ignores the small noise and focuses on the "big fish" (objects with an area > 500).

## 🛠️ Tech Stack

We're keeping it lean and mean:
*   **Python** (The brain)
*   **OpenCV** (The eyes)
*   **NumPy** (The math wizard)

## 🚀 How to Launch

1.  **Clone this beauty:**
    ```bash
    git clone https://github.com/yourusername/obstacle_detection.git
    cd obstacle_detection
    ```

2.  **Feed it dependencies:**
    ```bash
    pip install opencv-python numpy
    ```

3.  **Ignition:**
    ```bash
    python main.py
    ```

## 🎮 Controls

*   **`q`**: The "Get me out of here!" key (Quits the app).
*   **`c`**: The "Fresh Start" key (Clears your movement trail).
*   **Move something blue**: The "Have Fun" action!

## 🤝 Contributing

Got an idea to make it track Red? Green? Or maybe make it shoot lasers? (Okay, maybe not lasers... yet). Feel free to fork, star, and send pull requests. Let's make this even cooler together!

---
*Built with ❤️ CodeAkdo and a lot of blue objects.*
