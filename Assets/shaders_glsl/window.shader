//window.shader

varying vec2 Texcoord0;

#ifdef VERTEX_SHADER

uniform mat4 matScreenAligned;

void main()
{
	gl_Position = matScreenAligned * gl_Vertex;
	Texcoord0 = gl_MultiTexCoord0.xy;
}
#endif

#ifdef FRAGMENT_SHADER

uniform sampler2D tex0;
uniform float fade;

void main()
{
	gl_FragColor = texture2D(tex0, Texcoord0);
	gl_FragColor.rgb *= fade;
}
#endif
