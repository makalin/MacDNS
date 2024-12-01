# DNS Switcher for macOS

A lightweight and user-friendly menu bar application for macOS that allows quick switching between popular DNS providers. Easily toggle between Cloudflare, Google, and Quad9 DNS servers with just a click.

## Features

- 🔄 Quick DNS switching from the menu bar
- 🔒 Secure switching with administrator privileges
- 🎯 Support for popular DNS providers:
  - Cloudflare (1.1.1.1)
  - Google (8.8.8.8)
  - Quad9 (9.9.9.9)
- 📱 Native macOS menu bar integration
- 🔔 System notifications for DNS changes
- 👁 Visual indication of current DNS provider
- 🚀 Automatic startup option
- 💻 Works with Wi-Fi connections

## Requirements

- macOS 10.12 or later
- Python 3.6 or later
- Administrator privileges (for changing DNS settings)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/macdns.git
cd macdns
```

2. Install the required dependencies:
```bash
pip3 install rumps pyobjc
```

3. Make the script executable:
```bash
chmod +x macdns.py
```

4. Add an icon file:
- Place a PNG file named `icon.png` in the same directory as the script
- Recommended size: 32x32 pixels

## Usage

1. Start the application:
```bash
./macdns.py
```

2. Click the menu bar icon to see available DNS options
3. Select your desired DNS provider
4. Enter administrator password when prompted
5. Wait for the confirmation notification

### Auto-start Configuration

To make DNS Switcher start automatically on login:

1. Open System Preferences
2. Navigate to Users & Groups
3. Select your user account
4. Click the "Login Items" tab
5. Click the "+" button
6. Navigate to and select the macdns.py file

## DNS Providers

### Cloudflare
- Primary: 1.1.1.1
- Secondary: 1.0.0.1
- Features: Fast, privacy-focused

### Google
- Primary: 8.8.8.8
- Secondary: 8.8.4.4
- Features: Reliable, widely used

### Quad9
- Primary: 9.9.9.9
- Secondary: 149.112.112.112
- Features: Security-focused, malware blocking

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

### Development Setup

1. Set up a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

3. Run tests:
```bash
python -m pytest tests/
```

## Security

- The application requires administrator privileges only when changing DNS settings
- All DNS changes are logged and notified to the user
- No data collection or external connections besides DNS configuration

## Troubleshooting

### Common Issues

1. **"Permission denied" error**
   - Ensure the script has executable permissions
   - Run with administrator privileges when changing DNS

2. **Icon not showing**
   - Verify icon.png exists in the correct directory
   - Check icon file format and size

3. **DNS not changing**
   - Verify Wi-Fi is connected
   - Check administrator password is correct
   - Ensure no system DNS locks are in place

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [rumps](https://github.com/jaredks/rumps) for macOS menu bar integration
- DNS providers for their public DNS services
- Contributors and testers

## Version History

- 1.0.0 (2024-01-01)
  - Initial release
  - Basic DNS switching functionality
  - Menu bar integration

## Contact

- Create an issue for bug reports or feature requests
- Submit pull requests for contributions
