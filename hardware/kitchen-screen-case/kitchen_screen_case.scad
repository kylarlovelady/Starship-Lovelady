// Kitchen touch-screen case v4: thin, symmetric frame for the GeekPi 10.1 in screen (235 x 142 x 8 mm).
// The Pi 5 stays in its own kit case and is TAPED to the back plate (or the screen back) wherever it fits: no Pi geometry in this file.
// Cables go into the screen ports with 90-degree plugs that exit toward the back, then run straight back and across the open space behind the screen.
// Two printed parts: FRAME (front lip + thin walls all the way back) and BACK (plate + alignment rim + screen posts + feet).
// Join: 4 x M2.5 x 8 self-tapping screws from the top/bottom edges into bosses on the BACK rim. Screen: 4 x M2.5 x 12 from the wall side into the screen's rear holes.
// part = "frame" | "back" | "both".   Units mm.   Not test-compiled: open in OpenSCAD, F5, check for errors.
part = "both";

scr_w = 235; scr_h = 142; scr_t = 8;
bezel_cover = 4;      // front lip overlap (CHECK against the real black border)
fit = 0.4; wall = 2.4; lip = 2.0; corner = 5;
back_t = 2.6;
rear_room = 34;       // depth behind the screen: Pi kit case about 31 mm tall + 3 mm. (CHECK the real case; set to its height + 3)
foot_h = 4;           // feet: air gap behind the case and room for the wall-screw heads

hole_in = 7;          // M2.5 screen hole distance from each screen corner (ESTIMATE, CHECK)
port_top = 20;  port_bot = 123;   // ports run from 20 to 112 mm below the screen's top edge (switch 25, audio 53, USB-C 72, HDMI 106; ESTIMATES)
pocket_d = 18;        // how far the plugs stick out past the screen's left edge with 90-degree plugs (CHECK)
spk_a = 54; spk_b = 175;          // speaker centers from the right edge, back view
keyhole_dx = 150; keyhole_y = 60;
m25 = 2.5; m3 = 3.0;

out_w = scr_w + 2*(fit+wall);
out_h = scr_h + 2*(fit+wall);
z_s = back_t + rear_room;             // plane of the back of the screen
z_f = z_s + scr_t + lip + 0.6;        // front face
$fn = 40;

module rbox(w, h, d, r) { linear_extrude(d) offset(r=r) square([w-2*r, h-2*r], center=true); }
module posts() { for (sx=[-1,1], sy=[-1,1]) translate([sx*(scr_w/2-hole_in), sy*(scr_h/2-hole_in), 0]) children(); }
py0 = scr_h/2 - port_bot;  py1 = scr_h/2 - port_top;     // port zone, y range (front view, up is +)
pocket_x = -(scr_w/2 + fit);                              // the screen's left edge (the port edge)

// FRAME: z = 0 is the wall side of the plate position. Built back to front: z from back_t up to z_f.
module frame() {
  translate([0,0,back_t]) difference() {
    union() {
      rbox(out_w, out_h, z_f-back_t, corner);
      // port pocket: thin bulge on the left wall behind the screen only (invisible from the front)
      translate([pocket_x-pocket_d-wall/2, (py0+py1)/2, 0]) linear_extrude(rear_room) offset(r=3) square([pocket_d+wall, py1-py0+6], center=true);
    }
    translate([0,0,-1]) rbox(scr_w+2*fit, scr_h+2*fit, rear_room+scr_t+2, corner-2);        // screen pocket and rear space
    translate([pocket_x-pocket_d/2-wall/2+0.2, (py0+py1)/2, -1]) linear_extrude(rear_room+scr_t+2) offset(r=2) square([pocket_d+0.4, py1-py0+2], center=true); // port pocket cavity
    translate([0,0,z_f-back_t-lip-1]) rbox(scr_w-2*bezel_cover, scr_h-2*bezel_cover, lip+3, 2); // front window
    // vents: slanted slots in the top and bottom walls (warm air out the top, cool air in the bottom)
    for (i=[0:6]) translate([-105+i*9, out_h/2-wall/2, rear_room/2]) rotate([0,0,20]) cube([2.6, wall+3, rear_room-14], center=true);
    for (i=[0:6]) translate([-105+i*9, -out_h/2+wall/2, rear_room/2]) rotate([0,0,-20]) cube([2.6, wall+3, rear_room-14], center=true);
    // speaker sound slots in the top wall, above each speaker (speakers are on the back of the screen)
    for (c=[scr_w/2-spk_a, scr_w/2-spk_b]) translate([c, out_h/2-wall/2, rear_room+0.2-5]) cube([26, wall+3, 8], center=true);
    // power cord notch in the bottom wall (move x to suit the Pi position)
    translate([-45, -out_h/2+wall/2, 9]) cube([16, wall+3, 14], center=true);
    // frame screws: 2 on the top edge, 2 on the bottom edge
    for (sx=[-1,1], sy=[-1,1]) translate([sx*60, sy*(out_h/2-wall/2), 7]) rotate([sy*90,0,0]) cylinder(d=m25+0.2, h=wall+2, center=true);
  }
  // fine accent line on the front
  translate([0,0,z_f]) difference() {
    linear_extrude(0.6) offset(r=corner-1.2) square([out_w-2*corner-2.4, out_h-2*corner-2.4], center=true);
    translate([0,0,-1]) linear_extrude(3) offset(r=corner-2.6) square([out_w-2*corner-5.6, out_h-2*corner-5.6], center=true);
  }
}

// BACK: plate, a thin alignment rim that slides inside the frame walls, 4 screen posts, feet, vents.
module back() {
  difference() {
    union() {
      rbox(out_w, out_h, back_t, corner);                                   // plate (z 0..back_t)
      difference() {                                                        // rim
        translate([0,0,back_t]) rbox(scr_w+2*fit-0.4, scr_h+2*fit-0.4, rear_room-0.6, corner-2);
        translate([0,0,back_t-1]) rbox(scr_w-6, scr_h-6, rear_room+2, corner-2);
        translate([pocket_x-pocket_d/2, (py0+py1)/2, back_t-1]) cube([pocket_d*2+4, py1-py0+2, rear_room+2], center=true);   // open the rim at the ports
        for (c=[scr_w/2-spk_a, scr_w/2-spk_b]) translate([c, scr_h/2, back_t+rear_room-4.8]) cube([26,12,8], center=true);   // speaker windows in the rim
        for (sy=[-1,1]) translate([-78, sy*scr_h/2, back_t+rear_room/2]) cube([68,12,rear_room-10], center=true);          // vent windows in the rim
      }
      posts() translate([0,0,back_t]) cylinder(d=7, h=rear_room-0.3);       // screen posts end 0.3 mm short of the screen back (clamp with the screws)
      for (sy=[-1,1], sx=[-1,1]) translate([sx*60, sy*(scr_h/2-4), back_t]) cylinder(d=7, h=14);   // frame screw bosses, inside the rim
      for (sx=[-1,1], sy=[-1,1]) translate([sx*(out_w/2-14), sy*(out_h/2-14), -foot_h]) cylinder(d=12, h=foot_h+0.01);   // feet
    }
    // intake grille in the plate under the Pi kit case (default spot: left strip, portrait, x -114..-52, y -40..52); move it if the Pi goes elsewhere
    for (i=[-3:3]) translate([-83+i*8-1.5, -36, -1]) cube([3, 84, back_t+2]);
    // keyholes
    for (sx=[-1,1]) translate([sx*keyhole_dx/2, keyhole_y, -0.1]) { cylinder(d=9, h=back_t+0.2); translate([0,-4.5,(back_t+0.2)/2]) cube([4.5,9,back_t+0.2], center=true); }
    // screen screws: through plate and post, head recess on the wall side
    posts() { translate([0,0,-1]) cylinder(d=m25+0.3, h=rear_room+back_t+2); translate([0,0,-1]) cylinder(d=5, h=2.2); }
    // pilot holes for the frame screws in the bosses
    for (sx=[-1,1], sy=[-1,1]) translate([sx*60, sy*67, back_t+7]) cube([2,9,2], center=true);
  }
}

if (part == "frame") frame();
else if (part == "back") back();
else { frame(); back(); }
