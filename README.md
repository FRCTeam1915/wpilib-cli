<div align="center">
    <a href="https://mckinleyfirebirds.com">
        <picture>
            <img alt="WPILib-CLI" src="https://raw.githubusercontent.com/FRCTeam1915/wpilib-cli/refs/heads/main/assets/logo.svg" height="128px">
        </picture>
    </a>
    <h1>WPILib-CLI</h1>
</div>

🛠️WPILib-CLI is a command-line tool to generate new [WPILib](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/wpilib-setup.html) robotics projects.

## 🚀 Local Development

```bash
git clone https://github.com/FRCTeam1915/wpilib-cli.git
# Depending on your system, it's either pip or pip3
pip install -e .
wpilib-cli --help
```

## Working in progress...

> [!IMPORTANT]
> You can now generate a Command Based Skeleton project
> It will now build the project automatically after the creation

## Supported Languages
| Language | Support Status                                                               |
|----------|------------------------------------------------------------------------------|
| Java     | **Partial support** — project creation works... Still working in progress... |

## Supported Vendor Extensions
| Extension  | Description                                 |
|------------|---------------------------------------------|
| Phoenix 5  | CTRE motor controller library (version 5.x) |
| Phoenix 6  | CTRE motor controller library (version 6.x) |
| RevLib     | REV Robotics hardware libraries             |


> [!NOTE]
> If PyCharm says unresolved reference about something, right click the `src` folder and select `Mark Directory as > Sources Root` then restart PyCharm.
