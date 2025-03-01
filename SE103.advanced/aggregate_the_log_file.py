LOG_FILE_CONTENT = """
*.amazon.co.uk    89
*.doubleclick.net    139
*.fbcdn.net    212
*.in-addr.arpa    384
*.l.google.com    317
1.client-channel.google.com    110
6.client-channel.google.com    45
a.root-servers.net    1059
apis.google.com    43
clients4.google.com    71
clients6.google.com    81
connect.facebook.net    68
edge-mqtt.facebook.com    56
graph.facebook.com    150
mail.google.com    128
mqtt-mini.facebook.com    47
ssl.google-analytics.com    398
star-mini.c10r.facebook.com    46
staticxx.facebook.com    48
www.facebook.com    178
www.google.com    162
www.google-analytics.com    127
www.googleapis.com    87
"""


def count_domains(log_file, min_hits = 0 ):
  access_times = []
  website = []
  separate =   log_file.strip().split('\n')
  print(separate)
  for url in separate:
    domain_view = (url.split(' '))
    print(domain_view)
    access_times.append(domain_view[-1])
    website.append(domain_view[0])
   # website.split('.')
    #domain_view.remove()
  print(access_times)
  print(website)

def main():
  print(LOG_FILE_CONTENT)
  log_file = LOG_FILE_CONTENT
  min_hits = int(input("Enter the minimum hits you will like to see: " ))
  count_domains(log_file, min_hits= 2)



if __name__ == "__main__":
  main()
