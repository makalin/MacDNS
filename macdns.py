#!/usr/bin/env python3
import rumps
import subprocess
import os

class DNSSwitcherApp(rumps.App):
    def __init__(self):
        super(DNSSwitcherApp, self).__init__("DNS", icon="icon.png")
        
        # DNS configurations
        self.dns_configs = {
            "Cloudflare": ["1.1.1.1", "1.0.0.1"],
            "Google": ["8.8.8.8", "8.8.4.4"],
            "Quad9": ["9.9.9.9", "149.112.112.112"]
        }
        
        # Create menu items
        self.current_dns = None
        self.menu_items = {}
        for dns_name in self.dns_configs:
            menu_item = rumps.MenuItem(dns_name, callback=self.switch_dns)
            self.menu_items[dns_name] = menu_item
            self.menu.add(menu_item)
            
        # Add separator and status item
        self.menu.add(rumps.separator)
        self.status_item = rumps.MenuItem("Current DNS: Unknown")
        self.menu.add(self.status_item)
        
        # Check current DNS on startup
        self.check_current_dns()

    def check_current_dns(self):
        """Check current DNS servers and update menu accordingly"""
        try:
            # Get current DNS servers using networksetup
            cmd = ["networksetup", "-getdnsservers", "Wi-Fi"]
            result = subprocess.run(cmd, capture_output=True, text=True)
            current_servers = result.stdout.strip().split("\n")
            
            # Update menu items and status
            found_match = False
            for dns_name, servers in self.dns_configs.items():
                if servers[0] in current_servers:
                    self.menu_items[dns_name].state = 1
                    self.current_dns = dns_name
                    self.status_item.title = f"Current DNS: {dns_name}"
                    found_match = True
                else:
                    self.menu_items[dns_name].state = 0
                    
            if not found_match:
                self.status_item.title = "Current DNS: Custom/Other"
                
        except Exception as e:
            self.status_item.title = "Error checking DNS"
            print(f"Error checking DNS: {e}")

    def switch_dns(self, sender):
        """Switch DNS servers when menu item is clicked"""
        try:
            dns_name = sender.title
            dns_servers = self.dns_configs[dns_name]
            
            # Need sudo privileges to change DNS
            cmd = [
                "sudo", "networksetup",
                "-setdnsservers", "Wi-Fi"
            ] + dns_servers
            
            # Use osascript to prompt for password
            sudo_cmd = " ".join(cmd)
            apple_script = f'''
            do shell script "{sudo_cmd}" with administrator privileges
            '''
            
            subprocess.run(["osascript", "-e", apple_script])
            
            # Update menu state
            self.check_current_dns()
            rumps.notification(
                "DNS Switcher",
                "DNS Changed Successfully",
                f"Switched to {dns_name} DNS servers"
            )
            
        except Exception as e:
            rumps.notification(
                "DNS Switcher",
                "Error",
                f"Failed to switch DNS: {e}"
            )

if __name__ == "__main__":
    DNSSwitcherApp().run()
