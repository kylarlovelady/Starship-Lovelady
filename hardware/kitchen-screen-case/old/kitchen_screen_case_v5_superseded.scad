// Kitchen touch-screen case v5: screwed-on front faceplate, two hinged service doors, vents.
// Screen: GeekPi 10.1 in, 235 x 142 x 8 mm, all ports on its LEFT edge (front view). Pi 5 stays in its kit case, taped behind the screen.
// Parts (print black ASA):  BODY (back plate, walls, screen posts, feet)   FACEPLATE (front, screws on)   DOOR_LEFT (ports door)   DOOR_BOTTOM (Pi door)
// Hardware: faceplate 8 x M2.5 x 12 black (same kit as the screen screws; heads sit in counterbores)   screen 4 x M2.5 x 12   hinge pins 4 x M3 x 30 (your screws), nut traps not modelled: use a nut or a dab of glue at the end
// part = "body" | "faceplate" | "door_left" | "door_bottom" | "both" (assembled preview).   Units mm.
// NOT test-compiled (no OpenSCAD available here): open it, press F5, fix any error, and test-print ONE hinge first.
part = "both";

scr_w = 235; scr_h = 142; scr_t = 8;
bezel_cover = 4;      // faceplate lip over the screen's black border (CHECK)
fit = 0.4; wall = 6; corner = 6;
back_t = 2.6; rear_room = 34;   // rear_room = Pi kit case height 31 + 3 (CHECK)
plate_t = 4; foot_h = 4;
hole_in = 7;                    // M2.5 screen holes from each screen corner (ESTIMATE, CHECK)
// ports, measured down from the screen's top edge (ESTIMATES from the maker's diagram)
port_top = 20; port_bot = 123;
pocket_d = 18;                  // plug room past the screen's left edge
spk_a = 54; spk_b = 175;        // speaker centers from the right edge, back view
keyhole_dx = 150; keyhole_y = 60;
pin_len = 30;                   // M3 x 30 hinge pins

out_w = scr_w + 2*(fit+wall);
out_h = scr_h + 2*(fit+wall);
z_s = back_t + rear_room;       // back face of the screen
z_top = z_s + scr_t + 0.4;      // top of the body walls (faceplate sits here)
py0 = scr_h/2 - port_bot;  py1 = scr_h/2 - port_top;
x_scr = -(scr_w/2 + fit);       // screen's left edge
xo = x_scr - pocket_d - wall;   // outer face of the left pocket bump
yo = -out_h/2;                  // outer face of the bottom wall
rk = 4.5; kn = 9.4; kg = 0.3;   // hinge knuckle radius, knuckle length, gap
zh = back_t + 4.5;              // hinge axis height (hinges sit at the BACK edge of each door)
pocket_top = z_s + 5;
$fn = 40;

module rbox(w, h, d, r) { linear_extrude(d) offset(r=r) square([w-2*r, h-2*r], center=true); }
module posts() { for (sx=[-1,1], sy=[-1,1]) translate([sx*(scr_w/2-hole_in), sy*(scr_h/2-hole_in), 0]) children(); }

// ---------- hinge pieces, built in a LOCAL frame: X along the hinge, Y outward from the outer face (wall is Y -wall..0), Z real height ----------
function hstarts(L) = [0, L-pin_len];
module body_hinge(L) {          // fixed knuckles (bulges on the wall)
  for (a=hstarts(L)) for (k=[0, kn+kg+kn+kg]) translate([a+k, -wall/2, zh]) rotate([0,90,0]) cylinder(r=rk, h=kn);
}
module body_cut(L, zhi) {       // door opening, door-knuckle slots, pin holes
  zlo = zh + 5;
  translate([-0.3, -wall-0.1, zlo-0.3]) cube([L+0.6, wall+0.2, zhi-zlo+0.6]);
  for (a=hstarts(L)) {
    translate([a+kn+kg-0.3, -wall/2, zh]) rotate([0,90,0]) cylinder(r=rk+0.4, h=kn+0.6);
    translate([a+kn+kg-0.3, -wall-0.1, zh]) cube([kn+0.6, wall+0.2, 5.1]);
    translate([a-0.5, -wall/2, zh]) rotate([0,90,0]) cylinder(d=3.4, h=pin_len+1);
  }
}
module door_local(L, zhi) {     // the door itself
  zlo = zh + 5;
  difference() {
    union() {
      translate([0, -wall, zlo]) cube([L, wall, zhi-zlo]);
      for (a=hstarts(L)) {
        translate([a+kn+kg, -wall/2, zh]) rotate([0,90,0]) cylinder(r=rk-0.1, h=kn);
        translate([a+kn+kg, -wall, zh]) cube([kn, wall, 5.2]);
      }
    }
    for (a=hstarts(L)) translate([a-0.5, -wall/2, zh]) rotate([0,90,0]) cylinder(d=3.4, h=pin_len+1);
    children();
  }
}
// local-to-world placements
module at_left()   { multmatrix([[0,-1,0,xo],[1,0,0,py0],[0,0,1,0],[0,0,0,1]]) children(); }
bx0 = -112; bL = 76;
module at_bottom() { multmatrix([[1,0,0,bx0],[0,-1,0,yo],[0,0,1,0],[0,0,0,1]]) children(); }
Ll = py1 - py0;  zhi_l = pocket_top;
zhi_b = z_s - 2;

// ---------- parts ----------
module body() {
  difference() {
    union() {
      rbox(out_w, out_h, z_top, corner);
      translate([xo, py0-wall, 0]) cube([x_scr - xo + 6, Ll + 2*wall, z_top]);        // left pocket bump (rear half and up to the top)
      for (sx=[-1,1], sy=[-1,1]) translate([sx*(out_w/2-16), sy*(out_h/2-16), -foot_h]) cylinder(d=14, h=foot_h+0.01);   // feet
      at_left() body_hinge(Ll);
      at_bottom() body_hinge(bL);
    }
    translate([0,0,back_t]) rbox(scr_w+2*fit, scr_h+2*fit, z_top, 2);                // screen pocket and rear space
    translate([xo+wall, py0, back_t]) cube([x_scr - (xo+wall) + 1, Ll, pocket_top-back_t]);   // plug pocket cavity
    at_left() body_cut(Ll, zhi_l);
    at_bottom() body_cut(bL, zhi_b);
    // exhaust slots (angled) in the top wall, far from the screws and the speakers
    for (i=[0:4]) translate([-115+i*9, out_h/2-wall/2, back_t+rear_room/2]) rotate([0,0,20]) cube([2.6, wall+3, rear_room-14], center=true);
    // speaker sound slots in the top wall above each speaker
    for (c=[scr_w/2-spk_a, scr_w/2-spk_b]) translate([c, out_h/2-wall/2, z_s-4.5]) cube([26, wall+2, 8], center=true);
    // fan grille in the plate under the Pi kit case (default: left strip, portrait)
    for (i=[-3:3]) translate([-83+i*8-1.5, -36, -1]) cube([3, 84, back_t+2]);
    // wall keyholes
    for (sx=[-1,1]) translate([sx*keyhole_dx/2, keyhole_y, -0.1]) { cylinder(d=9, h=back_t+0.2); translate([0,-4.5,(back_t+0.2)/2]) cube([4.5,9,back_t+0.2], center=true); }
    // faceplate pilot holes
    for (p=fplate_pts()) translate([p[0], p[1], z_top-14]) cylinder(d=2.2, h=15);
  }
  // screen posts (added after the cavity cut), each with an M2.5 hole and a wall-side head recess
  posts() difference() {
    translate([0,0,back_t-0.01]) cylinder(d=7, h=rear_room-0.3);
    translate([0,0,-1]) cylinder(d=2.8, h=rear_room+back_t+2);
  }
}
function fplate_pts() = concat(
  [for (x=[-20,40,100], y=[-1,1]) [x, y*(out_h/2-wall/2)]],
  [for (y=[-40,40]) [out_w/2-wall/2, y]]);

module faceplate() {
  difference() {
    rbox(out_w, out_h, plate_t, corner);
    translate([0,0,-1]) rbox(scr_w-2*bezel_cover, scr_h-2*bezel_cover, plate_t+2, 2);
    for (p=fplate_pts()) translate([p[0], p[1], 0]) { translate([0,0,-1]) cylinder(d=2.8, h=plate_t+2); translate([0,0,plate_t-2.2]) cylinder(d=5, h=2.3); }
  }
}

module door_left() { door_local(Ll, zhi_l) {} }
module door_bottom() {
  door_local(bL, zhi_b) {
    for (i=[0:5]) translate([8+i*10, 1, 24]) rotate([90,0,0]) rotate([0,0,20]) cube([2.6, 12, 12], center=true);   // intake slots
    translate([bL/2, 1, 18]) rotate([90,0,0]) cylinder(d=9, h=wall+3);                                           // power cord hole (move to suit)
  }
}

if (part == "body") body();
else if (part == "faceplate") faceplate();
else if (part == "door_left") door_left();
else if (part == "door_bottom") door_bottom();
else { body(); translate([0,0,z_top]) faceplate(); at_left() door_local(Ll, zhi_l) {}; at_bottom() door_bottom_local(); }
module door_bottom_local() { door_local(bL, zhi_b) {} }
