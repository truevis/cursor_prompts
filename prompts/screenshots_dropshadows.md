Add the same screenshot drop shadows used on https://elementwise.app/


Standalone screenshots (figures and article images that sit on the page background, not inside a clipped card) get this on the img, not the figure or caption:



box-shadow: 0 24px 60px -24px rgba(0, 0, 0, 0.35);



Keep any existing border-radius. Do not add a new radius. Captions stay unshadowed.



Screenshots inside cards or other overflow:hidden frames will clip a box-shadow, because the img fills the frame and the padding is on the img. For those, add this class on the img instead:



.app-shot {

&#x20; filter: drop-shadow(0 12px 18px rgba(0, 0, 0, 0.28));

}



That shadow follows the opaque picture and shows in the padding around it. Leave the card's overflow and rounded corners as they are.



Apply this to product and UI screenshots only. Leave logos, portraits, icons, and portfolio photos unchanged.



Check the result in the browser. Confirm the computed shadow on a standalone screenshot and on a card screenshot, and confirm the card shadow is visible inside the frame rather than clipped away.

