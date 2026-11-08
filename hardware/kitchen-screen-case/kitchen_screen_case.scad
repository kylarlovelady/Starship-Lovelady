// Kitchen touch-screen case: GeekPi 10.1 in screen + bare Raspberry Pi 5 (4GB) with active cooler.
// Parametric OpenSCAD. Two printed parts: FRAME (front, holds the screen) and BACK (plate with keyholes and the Pi pod). 4 M3 screws join them.
// Set part = "frame", "back" or "both" (assembled preview). Print FRAME face-down; print BACK with the pod pointing up (the wall side up), light supports under nothing.
// ALL "MEASURE" values are estimates: measure the real screen with calipers and change them. Units: mm.

scr_w = 235;      // MEASURE screen outline width
scr_h = 142;      // MEASURE screen outline height
scr_t = 8;        // MEASURE screen thickness incl. glass
bezel_cover = 4;  // how much the front lip overlaps the screen edge (must NOT cover active pixels)
fit = 0.5;        // clearance around the screen
wall = 5.5;       // outer wall (thick enough to hold M3 screws in the side walls)
back_t = 2.4;     // back plate
rear_room = 6;    // space behind the screen for the screen back parts and the short flat cables
corner = 6;       // rounded corner radius

// Pi pod (the raised box on the back that holds the Pi, centered low)
pod_w = 104;      // pod outer width
pod_h = 72;       // pod outer height
pod_d = 24;       // pod extra depth behind the back plate (Pi 5 + cooler needs about 22)
pod_x = 0;        // shift of pod from center (left/right)
pod_y = -14;      // shift of pod from center (up/down)
pi_w = 85; pi_h = 56;   // Pi 5 board
pi_hole_dx = 58; pi_hole_dy = 49;  // Pi mounting hole spacing
standoff_h = 4; screw_d = 2.7;

// wall mount
keyhole_dx = 150;  // distance between the two keyhole slots at the top
keyhole_y  = 52;   // up from center

part = "both";
lip = 2.4;          // front lip thickness
m3 = 3.0;  // M3 screws go through the BACK rim into the FRAME side walls
screw_pts = [[-1,-0.5],[-1,0.5],[1,-0.5],[1,0.5]];  // x side, y fraction of half height

out_w = scr_w + 2*(fit+wall);
out_h = scr_h + 2*(fit+wall);
frame_d = lip + scr_t + 0.6;
back_d = back_t + rear_room;
$fn = 48;

module rbox(w, h, d, r) { linear_extrude(d) offset(r=r) square([w-2*r, h-2*r], center=true); }

// FRAME: z=0 is the front face, open toward the back (z = frame_d)
module frame() {
  difference() {
    union() {
      rbox(out_w, out_h, frame_d, corner);
    }
    // screen pocket (opens to the back)
    translate([0,0,lip]) rbox(scr_w+2*fit, scr_h+2*fit, frame_d, corner-2);
    // front window: lip covers only bezel_cover on each side
    translate([0,0,-1]) rbox(scr_w-2*bezel_cover, scr_h-2*bezel_cover, lip+2, 2);
    // blind screw holes in the side walls (M3 self-tapping into ASA)
    for (p=screw_pts) translate([p[0]*(out_w/2-wall/2), p[1]*out_h/2, frame_d-8]) cylinder(d=m3-0.4, h=9);
  }
  // fine accent line on the front face
  translate([0,0,-0.6]) difference() {
    linear_extrude(0.6) offset(r=corner-1.2) square([out_w-2*corner-2.4, out_h-2*corner-2.4], center=true);
    translate([0,0,-1]) linear_extrude(3) offset(r=corner-2.6) square([out_w-2*corner-5.6, out_h-2*corner-5.6], center=true);
  }
}

// BACK: z=0 touches the wall side of the plate region; pod points toward the wall (z negative)
module back() {
  difference() {
    union() {
      // plate
      rbox(out_w, out_h, back_t, corner);
      // rim that makes the rear room
      difference() { rbox(out_w, out_h, back_d, corner); translate([0,0,-1]) rbox(out_w-2*wall, out_h-2*wall, back_d+2, corner-2); }
      // pod behind the plate
      translate([pod_x, pod_y, -pod_d]) rbox(pod_w, pod_h, pod_d+0.01, 5);
    }
    // pod cavity, open into the rear room through the plate
    translate([pod_x, pod_y, -pod_d+wall]) rbox(pod_w-2*wall, pod_h-2*wall, pod_d+back_d, 3);
    // chimney vents: intake bottom, exhaust top (angled slots)
    for (sy=[-1,1]) translate([pod_x, pod_y+sy*(pod_h/2), -pod_d/2-1]) for (i=[-4:4]) translate([i*9,0,0]) rotate([0,0,sy*20]) cube([2.6, 12, pod_d-10], center=true);
    // side vents
    for (sx=[-1,1]) translate([pod_x+sx*(pod_w/2), pod_y, -pod_d/2-1]) for (i=[-2:2]) translate([0,i*10,0]) rotate([0,0,sx*20]) cube([12, 2.6, pod_d-10], center=true);
    // power cable notch (bottom edge, near the Pi's USB-C)
    translate([pod_x-pod_w/2+20, pod_y-pod_h/2, -pod_d/2-1]) cube([9, 14, 9], center=true);
    // wall keyholes
    for (sx=[-1,1]) translate([sx*keyhole_dx/2, keyhole_y, -0.1]) {
      cylinder(d=9, h=back_t+0.2);
      translate([0,-4.5,(back_t+0.2)/2]) cube([4.5,9,back_t+0.2], center=true);
    }
    // screw clearance holes at the rim corners, matching the frame side-wall holes
    for (p=screw_pts) translate([p[0]*(out_w/2-wall/2), p[1]*out_h/2, -1]) cylinder(d=m3+0.4, h=back_d+2);
  }
  // Pi standoffs on the pod floor; board bottom faces the wall
  translate([pod_x-pi_hole_dx/2, pod_y-pi_hole_dy/2, -pod_d+wall])
    for (dx=[0,pi_hole_dx], dy=[0,pi_hole_dy]) translate([dx,dy,0]) difference() { cylinder(d=6, h=standoff_h); translate([0,0,1]) cylinder(d=screw_d-0.4, h=standoff_h); }
}

if (part == "frame") frame();
else if (part == "back") back();
else { translate([0,0,back_d+frame_d]) mirror([0,0,1]) frame(); back(); }
