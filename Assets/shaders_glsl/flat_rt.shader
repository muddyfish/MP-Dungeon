//flat_rt.shader

varying vec2 Texcoord0;

#ifdef VERTEX_SHADER

uniform mat4 matWorld;
uniform mat4 matView;
uniform mat4 matProj;
uniform vec3 uvOffset;

void main()
{
	gl_Position = matProj * matView * matWorld * gl_Vertex;
	Texcoord0 = gl_MultiTexCoord0.xy + uvOffset.xy;
	Texcoord0.y = 0.78125 - Texcoord0.y;
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
