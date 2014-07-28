//display.shader

varying vec2 Texcoord0;

#ifdef VERTEX_SHADER

uniform mat4 matWorld;
uniform mat4 matView;
uniform mat4 matProj;

void main()
{
	gl_Position = gl_Vertex;
	Texcoord0 = gl_MultiTexCoord0.xy;
}
#endif

#ifdef FRAGMENT_SHADER

uniform sampler2D tex0;
uniform sampler2D tex1;

void main()
{
	gl_FragColor = texture2D(tex0, Texcoord0);
	gl_FragColor *= texture2D(tex1, Texcoord0);
}
#endif
