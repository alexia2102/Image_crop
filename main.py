from PIL import Image

def get_coordinates(corner, length, width, height):
    """
    Calculează coordonatele (x, y) pentru decuparea unui pătrat pe baza colțului ales.
    Args:
        corner (str): Colțul ales (stanga_sus, dreapta_sus, stanga_jos, dreapta_jos).
        length (int): Latura pătratului.
        width (int): Lățimea imaginii.
        height (int): Înălțimea imaginii.
    Returns:
        tuple: Coordonatele (x1, y1, x2, y2) pentru decupare.
    """
    if corner == "stanga_sus":
        return (0, 0, length, length)
    elif corner == "dreapta_sus":
        return (width - length, 0, width, length)
    elif corner == "stanga_jos":
        return (0, height - length, length, height)
    elif corner == "dreapta_jos":
        return (width - length, height - length, width, height)
    else:
        raise ValueError("Colț invalid! Alege dintre: stanga_sus, dreapta_sus, stanga_jos, dreapta_jos")

def main():
    # Încărcarea imaginii
    image_path = input("Introdu calea către imagine (ex: imagine.jpg): ").strip()
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Eroare la încărcarea imaginii: {e}")
        return
    
    width, height = image.size
    print(f"Dimensiunile imaginii: {width}x{height} pixeli")
    
    # Alegerea colțului
    print("Alege un colț pentru decupare: stanga_sus, dreapta_sus, stanga_jos, dreapta_jos")
    corner = input("Introdu numele colțului: ").strip().lower()

    # Alegerea lungimii pătratului
    try:
        length = int(input("Introdu lungimea laturii pătratului (pixeli): ").strip())
        if length <= 0 or length > min(width, height):
            raise ValueError("Lungimea trebuie să fie pozitivă și mai mică decât dimensiunile imaginii.")
    except ValueError as e:
        print(f"Eroare: {e}")
        return
    
    # Calcularea coordonatelor
    try:
        x1, y1, x2, y2 = get_coordinates(corner, length, width, height)
        print(f"Coordonatele decupării: ({x1}, {y1}, {x2}, {y2})")
    except ValueError as e:
        print(f"Eroare: {e}")
        return

    # Decuparea imaginii
    cropped_image = image.crop((x1, y1, x2, y2))
    cropped_image.show()  # Afișează imaginea decupată
    save_path = input("Introdu calea unde dorești să salvezi imaginea decupată (ex: decupat.jpg): ").strip()
    cropped_image.save(save_path)
    print(f"Imaginea a fost salvată la: {save_path}")

if __name__ == "__main__":
    main()
