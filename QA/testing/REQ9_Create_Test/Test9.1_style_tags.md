
## Author:
Sara Amaral

## Test scenario:
 Test the veracity of the classes container_tags, container_submit_cancel_tags, tag_button,tag_button:hover and tag_button_click as well as the elements test_title_box and CreateTest_instruction.
 
## Expected Result:
 Previously mentioned classes and elements display the visuals they intended to.

## Observed result:
 Container_tags creates a flexbox and makes all its contents, including children to begin at the top of the box and to be centered, as well as making their disposition be from left to right. 
  It also sets the gap between boxes, up, down, left, right to 50px. Note that the "row-gap" below is useless since the gap between rows was already set to the same velue by the line above.
  Gives the flexbox some margins as well.

  Container_submit_cancel_tags creates a flexbox and centers all its children both horizontally and vertically and makes them fit in the same row at the top of the flexbox. Also gives some margin to both left and right sides of the container.

  Tag_button changes the color of the background and gives a color to the continuous border around the button. Also sets the color of its text and other color-able items to blue.

  tag_button:hover Triggers when the mouse hovers over the tag button and when this happens the background color changes to white and the color and its border remain the same.

  tag_button_click, given that a "Click" selector does not exist, a whole class had to be created instead. However it does nothing visually as it has exactly the same characteristics as "tag_button:hover".

  test_title_box gives the height and margin exclusive to that one title box.

  CreateTest_instruction changes the background of that element.


