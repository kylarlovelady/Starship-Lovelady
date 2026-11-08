// Kitchen touch-screen case v3: GeekPi 10.1 in screen + bare Raspberry Pi 5 with active cooler.
// Dimensions from the maker's diagram: 235 x 142 x 8 mm. Ports are all on ONE short edge (the LEFT edge seen from the front):
//   volume/backlight switch, 3.5 mm audio out, ONE USB-C "Touch & Power", full-size HDMI-IN.
// v3: no protruding pod (v2 would have floated the whole case 24 mm off the wall). Uniform depth, Pi inside the slab.
// Two printed parts: FRAME (front, holds the screen with a lip) and BACK (plate with Pi pod). part = "frame" | "back" | "both".
// Screen is ALSO screwed to the BACK part with 4 x M2.5 through posts into the screen's rear holes (about 7 mm in from each corner: CHECK).
// Units mm. Not yet test-compiled in OpenSCAD: open it, press F5, look for errors before printing.

part = "both";

scr_w = 235; scr_h = 142; scr_t = 8;
bezel_cover = 4;      // lip overlap on the picture side edges (CHECK against the real black border)
fit = 0.5; wall = 5.5; back_t = 3.2; rear_room = 24; lip = 2.4; corner = 6;
bay_w = 46;           // extra width on the port side for plugs and cable bends (straight USB-A boot is about 24 mm, plus bend room)

// Screen mounting holes (M2.5), measured from each corner of the screen: ESTIMATE
hole_in = 7;
// Port heights measured DOWN from the top edge of the screen (from the maker's diagram, estimates)
port_switch = 25; port_audio = 53; port_usbc = 72; port_hdmi = 106;
// Speaker centers measured from the right edge in the BACK view
spk_a = 54; spk_b = 175;

// Pi 5 sits behind the screen, FLIPPED (cooler and ports toward the back plate), so its USB-A edge faces the cable bay,
// the power/HDMI edge faces down, and the cooler fan breathes through a grille in the back plate.
pi_w = 85; pi_h = 56; standoff_h = 17; pi_screw = 2.7;   // 17 mm: lets the cooler and USB ports clear the plate
pi_dx = 4;             // Pi left edge, measured from the screen's left edge (into the screen area)
pi_yb = -41;           // Pi bottom edge y (0 is the case center). 30.5 mm of room below it for the straight power plug
foot_h = 4;            // feet on the back: gives a 4 mm air gap and a floating look

keyhole_dx = 150; keyhole_y = 52;
m3 = 3.0; m25 = 2.5;
screw_pts = [[-1,-0.5],[-1,0.5],[1,-0.5],[1,0.5]];   // M3 frame-to-back screws in the side walls

out_w = scr_w + 2*(fit+wall) + bay_w;
out_h = scr_h + 2*(fit+wall);
sx0 = bay_w/2;                    // screen center x (screen sits to the right of the bay)
scr_x0 = sx0 - scr_w/2;           // x of the screen's left edge (the port edge)
frame_d = lip + scr_t + 0.6;
back_d = back_t + rear_room;
$fn = 40;

module rbox(w, h, d, r) { linear_extrude(d) offset(r=r) square([w-2*r, h-2*r], center=true); }
module at_posts() { for (sx=[-1,1], sy=[-1,1]) translate([sx0 + sx*(scr_w/2-hole_in), sy*(scr_h/2-hole_in), 0]) children(); }

module frame() {   // z = 0 is the front face, open toward the back
  difference() {
    rbox(out_w, out_h, frame_d, corner);
    translate([sx0, 0, lip]) rbox(scr_w+2*fit, scr_h+2*fit, frame_d, corner-2);               // screen pocket
    translate([-out_w/2+wall, 0, lip]) rbox(bay_w+2*fit+0.01, scr_h+2*fit, frame_d, 2);          // port bay
    translate([sx0, 0, -1]) rbox(scr_w-2*bezel_cover, scr_h-2*bezel_cover, lip+2, 2);          // front window
    for (i=[0:4]) translate([-out_w/2+wall+6+i*4.6, 0, -1]) cube([2.2, 52, lip+2]);            // decorative slots in the bay strip
    for (p=screw_pts) translate([p[0]*(out_w/2-wall/2), p[1]*out_h/2, frame_d-8]) cylinder(d=m3-0.4, h=9);
  }
  translate([0,0,-0.6]) difference() {   // thin accent line around the front
    linear_extrude(0.6) offset(r=corner-1.2) square([out_w-2*corner-2.4, out_h-2*corner-2.4], center=true);
    translate([0,0,-1]) linear_extrude(3) offset(r=corner-2.6) square([out_w-2*corner-5.6, out_h-2*corner-5.6], center=true);
  }
}

module back() {   // z = 0 is the wall-side face of the plate; feet extend toward the wall (negative z)
  difference() {
    union() {
      rbox(out_w, out_h, back_t, corner);
      difference() { rbox(out_w, out_h, back_d, corner); translate([0,0,-1]) rbox(out_w-2*wall, out_h-2*wall, back_d+2, corner-2); }
      at_posts() cylinder(d=7, h=back_d+0.5);                  // screen posts
      for (sx=[-1,1], sy=[-1,1]) translate([sx*(out_w/2-16), sy*(out_h/2-16), -foot_h]) cylinder(d=14, h=foot_h+0.01);   // feet
    }
    // fan intake grille in the plate, under the Pi's cooler (cooler is near the board center, estimate)
    translate([scr_x0+pi_dx+pi_w/2-1.5, pi_yb+pi_h/2-17, -1]) for (i=[-3:3]) translate([i*7, 0, 0]) cube([3, 34, back_t+2]);
    // exhaust: slanted slots in the top rim above the Pi, intake slots in the bottom rim
    for (i=[0:4]) translate([scr_x0+8+i*9, out_h/2-wall/2, back_t+rear_room/2+2]) rotate([0,0,20]) cube([2.6, wall+3, rear_room-8], center=true);
    for (i=[0:4]) translate([scr_x0+8+i*9, -out_h/2+wall/2, back_t+rear_room/2]) rotate([0,0,-20]) cube([2.6, wall+3, rear_room-8], center=true);
    // power cord notch in the bottom rim under the Pi's USB-C (flipped board: USB-C is about 74 mm from the Pi's left edge)
    translate([scr_x0+pi_dx+74, -out_h/2+wall/2, back_t+rear_room/2]) cube([16, wall+3, 12], center=true);
    // keyholes (screws in the wall; the 4 mm foot gap holds the screw heads)
    for (sx=[-1,1]) translate([sx*keyhole_dx/2, keyhole_y, -0.1]) { cylinder(d=9, h=back_t+0.2); translate([0,-4.5,(back_t+0.2)/2]) cube([4.5,9,back_t+0.2], center=true); }
    // M2.5 screen screws: hole through plate and post, head recess on the wall side
    at_posts() { translate([0,0,-1]) cylinder(d=m25+0.3, h=back_d+2); translate([0,0,-1]) cylinder(d=5, h=3); }
    // frame screws through the rim
    for (p=screw_pts) translate([p[0]*(out_w/2-wall/2), p[1]*out_h/2, -1]) cylinder(d=m3+0.4, h=back_d+2);
    // speaker sound slots in the top rim, above each speaker (speakers sit on the back of the screen, facing the plate)
    for (c=[sx0+(scr_w/2-spk_a), sx0+(scr_w/2-spk_b)]) translate([c, out_h/2-wall/2, back_t+rear_room-4.5]) cube([26, wall+2, 7], center=true);
  }
  // Pi standoffs: Pi 5 holes are 3.5 mm in from the board corners; flipped board puts them at 23.5 and 81.5 from the board's left edge
  for (hx=[pi_dx+23.5, pi_dx+81.5], hy=[pi_yb+3.5, pi_yb+52.5]) translate([scr_x0+hx, hy, back_t]) difference() { cylinder(d=6, h=standoff_h); translate([0,0,1]) cylinder(d=pi_screw-0.4, h=standoff_h); }
}

if (part == "frame") frame();
else if (part == "back") back();
else { translate([0,0,back_d+frame_d]) mirror([0,0,1]) frame(); back(); }
