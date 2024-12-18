### Detailed Documentation: Cropping a Square from an Image in Python

---

#### **1. Purpose of the Application**
This script allows the user to load an image, specify a corner of the image (e.g., top-left, bottom-right), and crop a square of a given size. The resulting image can be displayed and saved to a user-specified location.

---

#### **2. Libraries Used**
- **Pillow (`PIL`)**: A Python library for image processing. In this script, it is used to open, crop, and save images.

   Key functions used:
   - `Image.open(path)`: Opens the image file.
   - `Image.crop((x1, y1, x2, y2))`: Crops a rectangle specified by coordinates.
   - `Image.show()`: Displays the image in the default image viewer.
   - `Image.save(path)`: Saves the image to a specified file path.

---

#### **3. User Inputs**
The script asks the user for three pieces of information:
1. **Image Path**: The path to an existing image file (e.g., `image.jpg`).
2. **Image Corner**: The user can choose one of the four corners to crop from:
   - `top_left` (top-left corner of the image)
   - `top_right` (top-right corner of the image)
   - `bottom_left` (bottom-left corner of the image)
   - `bottom_right` (bottom-right corner of the image)
3. **Square Side Length**: The length of one side of the square to be cropped (in pixels).

---

#### **4. Coordinate Calculations**
To crop a square from the image, the script calculates the cropping rectangle's coordinates `(x1, y1, x2, y2)`, where:
- `(x1, y1)` represents the top-left corner of the square.
- `(x2, y2)` represents the bottom-right corner of the square.

The coordinates are calculated based on the corner chosen by the user:

| **Corner**       | **Description**                         | **Coordinate Formula**                    |
|-------------------|-----------------------------------------|-------------------------------------------|
| **top_left**      | The square starts at the top-left.      | `(0, 0, length, length)`                  |
| **top_right**     | The square starts at the top-right.     | `(width - length, 0, width, length)`      |
| **bottom_left**   | The square starts at the bottom-left.   | `(0, height - length, length, height)`    |
| **bottom_right**  | The square starts at the bottom-right.  | `(width - length, height - length, width, height)` |

---

#### **5. Validations and Restrictions**
To ensure correct execution, the script includes the following checks:
1. **Square Side Length**:
   - The square's side length must be **positive** and smaller or equal to the image dimensions:  
     Mathematically:  
     \[
     \text{length} \leq \min(\text{width}, \text{height})
     \]
2. **Valid Corner**:
   - The user must choose one of the valid corners: `top_left`, `top_right`, `bottom_left`, `bottom_right`.
3. **Image Path**:
   - The script checks whether the provided path points to a valid image file.

---

#### **6. Example of Execution**

Suppose we have an image with dimensions **800x600 pixels**.

- **User Inputs**:
   - Image path: `example.jpg`
   - Corner: `bottom_right`
   - Square side length: `200` pixels

- **Coordinate Calculation**:
   - Chosen corner: **bottom_right**  
   - Formula: `(width - length, height - length, width, height)`  
   - Result: `(800 - 200, 600 - 200, 800, 600)` → `(600, 400, 800, 600)`

- **Output**:
   - A square of dimensions **200x200 pixels** is cropped from the **bottom-right** corner of the image.

---

#### **7. Common Errors and Solutions**
1. **Error**: "The length must be positive and smaller than the image dimensions."  
   **Cause**: The square side length entered is invalid.  
   **Solution**: Verify the image dimensions and enter a valid length.

2. **Error**: "Invalid corner!"  
   **Cause**: The user entered a corner that is not recognized.  
   **Solution**: Enter one of the valid corners: `top_left`, `top_right`, `bottom_left`, or `bottom_right`.

3. **Error**: "Error loading the image."  
   **Cause**: The file path is incorrect, or the file does not exist.  
   **Solution**: Verify that the image exists and provide the correct path.

---

#### **8. Script Functions**
- **`get_coordinates(corner, length, width, height)`**:  
   Accepts the corner, square side length, and image dimensions, and returns the coordinates for cropping.

- **`main()`**:  
   The main function that:
   - Requests input from the user.
   - Calculates the cropping coordinates.
   - Crops the image using the `crop()` method.
   - Displays and saves the cropped image.

---

#### **9. Execution Flow Diagram**

```plaintext
+--------------------------+
| Load the image           |
+-----------+--------------+
            |
            v
+--------------------------+
| Choose corner and length |
+-----------+--------------+
            |
            v
+-------------------------------+
| Calculate (x1, y1, x2, y2)   |
+-----------+-------------------+
            |
            v
+-------------------------+
| Crop the square         |
+-----------+-------------+
            |
            v
+-------------------------+
| Show and save the image |
+-------------------------+
```

---

#### **10. How to Run the Script**
1. Install the Pillow library if not already installed:
   ```bash
   pip install pillow
   ```
2. Run the script:
   ```bash
   python script.py
   ```
3. Provide the required inputs:
   - Path to the image file.
   - Corner to crop from (`top_left`, `top_right`, `bottom_left`, `bottom_right`).
   - Square side length in pixels.
4. The cropped image will be displayed and saved to the specified location.

---

#### **11. Example Usage**

**Input**:  
```
Enter the image path (e.g., image.jpg): example.jpg  
Choose a corner for cropping: bottom_right  
Enter the square side length (in pixels): 200  
```

**Output**:  
The script calculates the coordinates, crops the image, and saves it.  

**Coordinates**: `(600, 400, 800, 600)`  
**Result**: A 200x200 pixel square cropped from the bottom-right corner.

---

#### **12. Conclusion**
This script is a simple yet effective tool for image processing. Users can specify a square's size and location (based on the image corners) to crop it efficiently. The code is modular, easy to understand, and can be extended to support additional features such as arbitrary rectangle cropping or graphical user interfaces.
