<div align="center">
    <a href="https://mckinleyfirebirds.com">
        <picture>
            <img alt="WPILib-CLI" src="https://raw.githubusercontent.com/FRCTeam1915/wpilib-cli/refs/heads/main/assets/logo.svg" height="128px">
        </picture>
    </a>
    <h1>WPILib-CLI</h1>
</div>

🛠️ WPILib-CLI is a command-line tool to generate new [WPILib](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/wpilib-setup.html) robotics projects.

## 🚀 Local Development

```bash
git clone https://github.com/FRCTeam1915/wpilib-cli.git
# Depending on your system, it's either pip or pip3
pip install -e .
wpilib-cli --help
```

## ⏳ Working in progress...

## 🗣️ Supported Languages
| Language | Support Status         |
|----------|------------------------|
| ☕ Java   | Working in progress... |

## 🔌 Supported Vendor Extensions
| Extension  | Description                         | Current URL                                                                                                             |
|------------|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| DogLog     | Logging library                     | https://doglog.dev/vendordep.json                                                                                       |
| Grapple    | LaserCAN                            | https://storage.googleapis.com/grapple-frc-maven/libgrapplefrc2025.json                                                 |
| MapleSim   | Simulation                          | https://shenzhen-robotics-alliance.github.io/maple-sim/vendordep/maple-sim.json                                         |
| Phoenix 5  | CTRE motor controller (version 5.x) | https://maven.ctr-electronics.com/release/com/ctre/phoenix/Phoenix5-frc2025-latest.json                                 |
| Phoenix 6  | CTRE motor controller (version 6.x) | https://maven.ctr-electronics.com/release/com/ctre/phoenix6/latest/Phoenix6-frc2025-latest.json                         |
| PhotonLib  | Photon Vision library               | https://maven.photonvision.org/repository/internal/org/photonvision/photonlib-json/1.0/photonlib-json-1.0.json          |
| ReduxLib   | Redux Robotics                      | https://frcsdk.reduxrobotics.com/ReduxLib_2025.json                                                                     |
| REVLib     | REV Robotics hardware libraries     | https://software-metadata.revrobotics.com/REVLib-2025.json                                                              |
| Studica    | VMX-pi or navX-MXP                  | https://raw.githubusercontent.com/FRCTeam1915/wpilib-cli-backend/refs/heads/extensions/extensions/Studica-2025.0.1.json |
| ThriftyLib | Nova motor controller               | https://docs.home.thethriftybot.com/ThriftyLib.json                                                                     |
| YAGSL      | Yet Another Generic Swerve Library  | https://broncbotz.org/YAGSL-Lib/yagsl/yagsl.json                                                                        |

> [!NOTE]
> It is impossible to install Studica via `./gradlew vendordep` because it will generate an http 403 error
>
> You guys suck Studica, please fix your Maven repository!

> [!IMPORTANT]
> An URL is wrong? Feel free to open a PR [here](https://github.com/FRCTeam1915/wpilib-cli-backend/tree/extensions)

## 📂 Supported Templates
| Name                 | Status |
|----------------------|--------|
| CommandBasedSkeleton | ✅      |
| Educational Robot    | ⚠️     |

> [!IMPORTANT]
> `Desktop Support` and `JUnit 5` are enabled by default


## 🎥 Little Demonstration
Check out this [video](https://www.youtube.com/watch?v=Y-nSDGd3G2A)!

> [!NOTE]
> Since this is just a toy project for recreational programming, Python should be good enough for now. My apologies for slow development! We're college students, and we need to prioritize school work and life!
