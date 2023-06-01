## mario platformer Demo
****![demo video](https://github.com/RoyLee1224/mario-platformer/blob/main/10%20-%20victory/graphics/demo/demo.gif)****

## 程式架構

**這些檔案分別代表遊戲中的不同部分和功能：**

1. `main.py`：遊戲的主文件，用於初始化遊戲、處理遊戲循環和遊戲狀態。
2. `level.py`：定義遊戲中的關卡類別和功能，包括關卡的建立、繪製和更新，以及玩家和敵人的互動。
3. `player.py`：此文件定義玩家角色的類別和功能，包括移動、跳躍等。
4. `enemy.py`：此文件定義敵人類別和功能，包括移動、攻擊等。
5. `overworld.py`：定義遊戲中的世界地圖類別和功能，用於在關卡之間進行導航。
6. `ui.py`：定義用戶界面的類別和功能，例如顯示玩家生命值、金幣數量等。
7. `support.py`：包含支持遊戲運行所需的輔助函數和類別。
8. `tiles.py`：此文件定義遊戲中的地板圖塊（例如草地、磚塊等）的類別和功能。
9. `decorations.py`：定義裝飾物類別（例如樹、花等），這些裝飾物為遊戲關卡增添美觀。
10. `particles.py`：定義粒子效果（例如塵土、火花等）的類別和功能，增強遊戲視覺效果。
11. `game_data.py`：包含遊戲數據（例如關卡數據、敵人數據等）的類別和函數。
12. `settings.py`：包含遊戲的基本設置，例如螢幕尺寸、顏色、圖像路徑等。
13. `transition.py` ：創建遊戲場景之間轉場效果。
14. `menu.py` ：遊戲的主選單介面
15. `victory.py` ：呈現遊戲的勝利畫面，結算金幣總數。

> 將遊戲代碼模組化，便於開發和維護。
> 

## ****The logic of the mario game****

1. Level setup
    1. Create a level class that contains the game and the sprite groups
    2. Create a class for the player and the level tiles
    3. Convert the layout to an actual level
2. Player movement
3. Collisions
4. Camera

[The logic of a 2D platformer in Python / Pygame](https://youtu.be/Gmrf_3LbXu0)

### 撰寫流程：

- [1 - Intro:](https://youtu.be/KJpP85tnOKg)
    
    
- [2 - Player creation:](https://youtu.be/YWN8GcmJ-jA)
    - Intro & overview
    - Setting up the level
    - Creating the player
    - Creating the player 'camera'
    - Making the player move and collide
    - Animating the player
    - Animation state management
    - Dust particle animations
- [3 - Level creation:](https://youtu.be/wJMDh9QGRgs)
    - Intro
    - Using Tiled to create a level
    - Exporting TIled CSV files
    - Setting up the level in pygame
    - Importing CSV files
    - Converting CSV data to usable positions
    - Importing a tilesheet and slicing it (+terrain placement)
    - Setting up all static layers
    - Creating and placing the animated tiles
    - Adding the sky, water and clouds
    - Integrating the player character
- [4 - Overworld:](https://youtu.be/IUe2pdTWroc)
    - Intro
    - Project preparation
    - The overworld logic
    - Game state management
    - adding graphics and integrating the level
- [5 - User interface:](https://youtu.be/4jdJhUfMycQ)
    - Intro
    - Project setup
    - Displaying the user interface
    - Updating the user interface
    - Player collisions with the enemies
    - Game over state management

## TO-DO:

1. Enable double jump
2. New levels
3. Optimize the player camera(adjust the camera border and add scroll_y)
4. Apply transitions instructions(level pass effect, game over effect, menu)
5. New enemies

## Assets:
****[Treasure Hunters](https://pixelfrog-assets.itch.io/treasure-hunters)****

## Reference:
[GitHub - clear-code-projects/2D-Mario-style-platformer](https://github.com/clear-code-projects/2D-Mario-style-platformer)

## New Levels:
****![level4](https://github.com/RoyLee1224/mario-platformer/blob/main/10%20-%20victory/graphics/level/level4.png)****
****![level5](https://github.com/RoyLee1224/mario-platformer/blob/main/10%20-%20victory/graphics/level/level5.png)****
****![level6](https://github.com/RoyLee1224/mario-platformer/blob/main/10%20-%20victory/graphics/level/level6.png)****


## 期末發表

- **專案主題：** 平台式冒險遊戲 - **"瑪利歐海賊團"**
- **目標：** 我們的目標是建立一款引人入勝、操作簡單難度適中的平台遊戲，體驗者在遊戲過程中需收集金幣、避開敵人，並成功通過六道關卡獲得勝利。
- **小組成員：**
    - 李喆宸 (貢獻度：35%) - 介面設計、遊戲機制優化、遊戲測試、文檔撰寫、簡報製作。
    - 馮德愛 (貢獻度：25%) - 關卡四設計
    - 李肇恆 (貢獻度：25%) - 關卡五設計
    - 梁辰 (貢獻度：15%) - 關卡六設計
- **創新性：** 提升遊戲流暢度、過場效果
- **技巧性：** 模組化，避免重複程式碼，架構清楚
- **完整性：** 完整包含主菜單、過場、關卡、結算，讓玩家有完整的遊戲體驗
- **外觀：** 使用遊戲專用資源包進行開發
- **優點：**
    - 使用遊戲資源包，符合實際的軟體開發分工
    - 重視細節（特製鼠標、轉場效果、文字特效）
    - 檔案分類清楚，架構明確
    - 留存檔案開發紀錄，比較容易除錯（有push上去github）
- **缺點與未來改進方向：** 關卡難度的平衡上還需要改進，未來版本可以增加更多的敵人類型和地圖物件。
