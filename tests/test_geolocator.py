from northstar_image_geolocation import geolocate_image

def test_geolocate_image():
    c = geolocate_image("street_photo.jpg")
    assert "estimated_lat" in c.result
    assert c.result["radius_km"] > 0
