# 🐍 Snake Game

A classic **Snake Game** built with Python's `turtle` graphics library. Navigate your snake, eat fruits, collect power-ups, and compete for high scores across 5 difficulty levels!

---

## 🎮 Features

- **5 Game Modes**: Easy, Medium, Hard, Extreme, and Impossible
- **Dynamic Gameplay**: 
  - Fruits spawn randomly on the board
  - Snake grows longer with each fruit eaten
  - Game speed increases progressively (after 10 and 25 fruits)
- **Power-ups** (30% chance after eating fruit):
  - 🔵 **Blue**: Adds 2 snake blocks + 2 points
  - 💚 **Dark Green**: Instant +5 points
  - 💜 **Purple**: Score multiplier boost (up to 5x)
- **Pause/Resume**: Hit spacebar to pause and unpause
- **High Score Tracking**: Automatically saves your best score to `highscore.txt`
- **Cheat Codes**: For testing and fun (press `/` during gameplay)
- **Smooth Controls**: Arrow keys or WASD for direction

---

## 🎯 How to Play

1. **Run the game**:
   ```bash
   python snake-game.py
   ```

2. **Select difficulty** when prompted (Easy → Impossible)

3. **Wait for the countdown** (3... 2... 1... Go!)

4. **Control your snake**:
   - **Arrow Keys** or **A/D** to move left/right
   - **Spacebar** to pause/unpause
   - **Q** to quit

5. **Game objectives**:
   - Eat red fruits to grow and score points
   - Collect colored power-ups for bonuses
   - Avoid hitting walls or yourself
   - Beat your high score!

---

## ⌨️ Controls

| Key | Action |
|-----|--------|
| ← / A | Turn Left |
| → / D | Turn Right |
| Spacebar | Pause/Resume |
| / | Activate Cheat Codes |
| Q | Quit Game |

---

## 💾 Cheat Codes

Press **/** during gameplay to enter cheat mode. Available codes:

- **`slow`** - Reduce game speed (0-10 centiseconds)
- **`setspeed`** - Set custom game speed (3-20 centiseconds)
- **`bigsnake`** - Add 10 blocks to your snake
- **`biggersnake`** - Add 25 blocks to your snake
- **`invincible`** - Disable collision detection
- **`disablecheat`** - Exit cheat mode

---

## 📋 Difficulty Levels

| Mode | Speed (seconds) | Description |
|------|-----------------|-------------|
| Easy | 0.075 | Perfect for beginners |
| Medium | 0.06 | Balanced challenge |
| Hard | 0.05 | For experienced players |
| Extreme | 0.04 | High-speed gameplay |
| Impossible | 0.03 | Maximum difficulty |

---

## 📊 Game Mechanics

### Scoring System
- **1 fruit** = 1 point (or multiplied by current multiplier)
- **Blue power-up** = +2 blocks + 2 points
- **Dark Green power-up** = +5 points
- **Purple power-up** = Score multiplier increases by 1 (max 5x)

### Speed Progression
- Base speed set by difficulty mode
- Speeds up by 0.004 sec after 10 fruits
- Speeds up by 0.006 sec after 25 fruits

### Collision Detection
- Game ends if snake hits walls (±300 boundary)
- Game ends if snake hits itself
- Invincible cheat disables collision

---

## 🛠️ Requirements

- **Python 3.6+**
- **turtle** module (built-in with Python)
- **highscore.txt** file (created automatically on first run)

---

## 📁 Project Structure

```
snake-game.py       # Main game file
highscore.txt       # Auto-generated high score storage
```

---

## 🚀 Getting Started

1. Clone or download this repository
2. Ensure `snake-game.txt` exists in the same directory (or it will be created)
3. Run the game:
   ```bash
   python snake-game.py
   ```

4. Play, pause, collect power-ups, and beat your high score!

---

## 🎨 Game Elements

- **Snake**: Green blocks (alternating dark green for visibility)
- **Fruits**: Red circles (spawn randomly)
- **Power-ups**: Blue, Purple, and Dark Green circles (random effects)
- **Board**: 600×600 pixel arena with white border

---

## 💡 Tips & Tricks

- **Early power-ups matter**: Collect them early to build your multiplier
- **Learn the speeds**: Higher difficulties require faster reflexes
- **Use corners**: Navigate into corners to avoid head-on collisions
- **Watch for spawns**: Be aware of where fruits and power-ups spawn

---

## 🐛 Known Issues

None currently! Report any bugs or issues you find.

---

## 📝 License

This project is open source and available under the MIT License.

---

## 👨‍💻 Author

Built with Python and the `turtle` graphics library.

**Have fun playing! 🎮**
