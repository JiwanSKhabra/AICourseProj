# Genshin Oculi Auto-Tracker (Mondstadt)

## Problem Statement
In Genshin Impact, Oculi are collectible items used to upgrade Statues of The Seven in each region. Upgrading these statues rewards the player with **Primogems**, a premium in-game currency used primarily for wishing (gacha pulls) to obtain new characters and weapons, which is a core motivation for many players. Due to the fact Primogems have real value in progression and character acquisition, missing an Oculi directly means missing out on rewards that impact gameplay and collection goals.

However, Oculi are scattered across large, complex open-world environments with no built-in in-game checklist. Most players rely on external interactive maps and must manually mark each Oculi as collected, which is tedious, easy to forget, and error-prone, especially when returning to the game after breaks or switching devices. This project aims to automatically detect when an Oculi is collected in real time and update a personal progress map, ensuring that players do no accidentally miss Primogems and can track their completion efficiently.

## Proposed Method
This project uses **computer vision (CV)** to detect the "Oculi Collected" pickup notification during gameplay. When detection occurs, the system mark the nearest uncollected Oculi on a custom we-based map. the map updates in real time, allowing players to visually track remaining Oculi without manual logging. The first phases will try to incorporate template mathcing for detection and a static map of Mondstadt Oculi coordinate dataset. Later phases might use more concrete way of collection and tracking.

## Data Sources
- An export of Mondstadt Oculi coordinates from the AppSample Genshin Impact Interactive Map (https://genshin-impact-map.appsample.com/)
- Gameplay screenshots captured during testing to build and refine detection templates

## Project Goals
- Detect Oculi collection reliably using CV
- Mark the corresponding Oculi on a live map UI 
- Save player progress locally to persist completed Oculi

## Future Goals
Support for additional regions (Liyue, Inazuma, Sumeru, Fontaine, Natlan)

