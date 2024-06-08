import datetime

class Firewall:
    def __init__(self, config_file):
        self.config = self.load_config(config_file)
        self.log_file = "firewall_logs.txt"

    def load_config(self, config_file):
        config = {}
        with open(config_file, "r") as f:
            for line in f:
                key, value = line.strip().split("=")
                config[key.strip()] = value.strip()
        return config

    def is_allowed(self, ip_address):
        # Check if the IP address is allowed based on configuration
        allowed_ips = self.config.get("allowed_ips", "").split(",")
        return ip_address in allowed_ips

    def log_visit(self, ip_address, device):
        # Log the visit along with IP, device, and time
        with open(self.log_file, "a") as f:
            f.write(f"IP: {ip_address}\nDEVICE: {device}\nTIME: {datetime.datetime.now()}\n\n")

def main():
    config_file = "firewall_config.txt"
    firewall = Firewall(config_file)

    # Simulate incoming traffic
    incoming_traffic = [
        {"ip_address": "192.168.1.1", "device": "Desktop"},
        {"ip_address": "10.0.0.1", "device": "Mobile"},
        {"ip_address": "172.16.0.1", "device": "Tablet"},
    ]

    for visit in incoming_traffic:
        ip_address = visit["ip_address"]
        device = visit["device"]

        if firewall.is_allowed(ip_address):
            firewall.log_visit(ip_address, device)
            print(f"Allowed: {ip_address} - {device}")
        else:
            print(f"Blocked: {ip_address} - {device}")

if __name__ == "__main__":
    main()
