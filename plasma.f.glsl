#version 110

varying vec2 uv;

uniform vec2 C1;
uniform vec2 C2;
uniform vec2 C3;

vec2 diff;
float dist;
float z;

void
main() {
	z = 0.;

	diff = C1 - uv;
	dist = sqrt(diff.x * diff.x + diff.y * diff.y);
	z += sin(3. * 2. * 3.141592 * dist);

	diff = C2 - uv;
	dist = sqrt(diff.x * diff.x + diff.y * diff.y);
	z += sin(3. * 2. * 3.141592 * dist);

	diff = C3 - uv;
	dist = sqrt(diff.x * diff.x + diff.y * diff.y);
	z += sin(3. * 2. * 3.141592 * dist);

	z = z / 3.;
	z = .5 * (z + 1.);

	z = sin(3. * 2. * 3.141592 * z);
	z = .5 * (z + 1.);

	vec4 color0 = vec4(1.0, 0.0, 0.0, 1.0);
	vec4 color1 = vec4(1.0, 1.0, 0.0, 1.0);
	
	gl_FragColor = mix(color0, color1, z);
}

