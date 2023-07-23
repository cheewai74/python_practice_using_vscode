from zeroconf import ServiceBrowser, ServiceListener, Zeroconf
import re


class MyListener(ServiceListener):
    
    def __init__(self):
        super().__init__()
        self._services = {}

    def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        print(f"Service {name} updated")

    def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        print(f"Service {name} removed")

    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        info = zc.get_service_info(type_, name)
        server_name = info.server.rstrip('.local.')
        print(f"Service {name} added, service info: {info}")
        services = self._services.setdefault(server_name, {})
        services[type_] = info
        # port = info.port
        # server = info.server
        print(services[type_])
        return services[type_]
            # print("Port:", port)
            

zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)
try:
    x = listener.add_service(zeroconf, '_http._tcp.local.', 'myrouter._http._tcp.local.')
    # k = { "port": x[0], "server": x[1] }
    print(x.port)
    # print(k.get("server"))
finally:
    zeroconf.close()