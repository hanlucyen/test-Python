int n= 120, c=82;
PVector t;
Pvector[] pos = new Pvector[n];
float x,y,angle;
void setup() {
	size(500,500);
	colorMode(HSB,360,100,100);
	for (int i=0; i<n; i++) {
		pos[i]=new PVector(
				width/2,height/2);
	}
}
void draw() {
	background(0);
	noStroke();
	x= width/2+cos(angle)*150;
	y= height/2+sin(angle*2)*150;
	t= new PVector(x,y);
	PVector l = new PVector(t.x,t.y);
	for(int i=0; i<n; i++) {
		fill(180.0/n*i,90,90);
		PVector p = pos[i];
		PVector d =PVector.sub(l,p);
		PVector v =PVector.mult(d,0.5);
		p.add(v);
		crircle(p.x,p.y,70);
		l = p;
	angle += PL/c;
	}
