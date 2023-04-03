```mermaid
    classDiagram
        Pelilauta "1" -- "40" Ruutu
        Pelinappula ..> Ruutu
        Pelinappula: +Ruutu sijainti
        Pelaaja "1" -- "1" Pelinappula
        note for Pelaaja "2-8 kappaletta"
        Pelaaja ..> Noppa
        Ruutu: +Ruutu seuraava
```