const fs=require('fs');
const s=fs.readFileSync('index.html','utf8');
const i=s.indexOf('id=\"view-education\"');
fs.writeFileSync('ed2.txt', s.substring(i-100, i+6000));
