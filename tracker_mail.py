import requests

def track_package(tracking_number):
    url = f"https://api.shippingcarrier.com/track/{tracking_number}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        status = data["status"]
        location = data["location"]
        estimated_delivery = data["estimated_delivery"]  #what
        
        print("Package Status:", status)
        print("Current Location:", location)
        print("Estimated Delivery:", estimated_delivery)
    else:
        print("Failed to track package. Please check the tracking number.")

# Пример использования
tracking_number = "123456789"  # Замените на свой трекинг-номер
track_package(tracking_number)
