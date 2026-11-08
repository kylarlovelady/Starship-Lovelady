// Example: a 60 x 40 x 12 mm bracket with two screw slots and a vent grid. Run: node --stack-size=30000 example-part.mjs
import {box,zcyl,stlBinary} from './csg.mjs';
import fs from 'fs';
let p=box(0,60,0,40,0,12);
p=p.sub(box(6,54,6,34,3,13));                                  // pocket
for(const x of [10,50]) p=p.sub(zcyl(x,20,2.6,-1,13,24));      // M5 holes
for(let i=0;i<5;i++) p=p.sub(box(14+i*7,16+i*7,12,28,-1,4));   // vent slots in the floor
fs.mkdirSync('stl',{recursive:true}); fs.writeFileSync('stl/example_bracket.stl',stlBinary(p.cleanTris())); console.log('wrote stl/example_bracket.stl');
