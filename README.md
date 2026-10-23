# Flappy Bird (Pygame)

A Flappy Bird clone written in Python with **Pygame**: dodge an endless stream of pipes, score a point for each one you pass, and try to beat your best run.

## How to play

| Key | Action |
|---|---|
| `↑` (or keypad `Enter`) | Start a game from the welcome screen |
| `Space` | Flap |
| `Esc` | Quit |

You crash if you hit a pipe, the ground or the top of the screen. Your score prints in the terminal and the game returns to the welcome screen.

## Run it

```bash
pip install pygame
python "flappy bird.py"
```

All sprites (`bird.png`, `pipe.png`, `background.jpeg`, …) are loaded from the same folder as the script.

## How it works

- **Game loop:** a fixed 50 FPS loop (`pygame.time.Clock`) redraws the background, pipes, ground and bird every frame.
- **Gravity and flap:** the bird falls a few pixels every frame. `Space` moves it up 50 px.
- **Pipes:** each pipe pair gets a random vertical offset (`getpipe`) with a fixed gap. Once a pair scrolls off-screen it respawns on the right, and you score a point.
- **Collision:** `Crash()` checks the bird's height against the top and bottom pipe while the pipe is inside the bird's column.
- **Sprites:** the top pipe is the bottom pipe image rotated 180° with `pygame.transform.rotate`.

## What I learned

My first real game loop: frame timing, event handling, sprite blitting, and simple collision detection. This is also where I learned that game "physics" is mostly small numbers tuned until it feels right.

## Ideas for next time

- Show the score and high score on screen instead of in the terminal
- Use rect-based collision (`pygame.Rect.colliderect`) instead of hand-tuned numbers
- Add the flap and point sounds
