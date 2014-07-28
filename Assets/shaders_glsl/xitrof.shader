//xitrof.shader

varying vec2 Texcoord0;

#ifdef VERTEX_SHADER

uniform mat4 matWorld;
uniform mat4 matView;
uniform mat4 matProj;
uniform vec3 uvOffset;

void main()
{
	vec4 wPos = matWorld * gl_Vertex;
	vec4 wp = matView * wPos;
	gl_Position = matProj * wp;
	Texcoord0 = gl_MultiTexCoord0.xy + uvOffset.xy;
}
#endif

#ifdef FRAGMENT_SHADER

uniform sampler2D tex0;
uniform float fade;
uniform vec4 materialDiffuse;

void main()
{
	gl_FragColor = texture2D(tex0, Texcoord0);
	gl_FragColor.rgb += materialDiffuse.rgb;
	gl_FragColor.rgb *= fade;
	gl_FragColor.a *= materialDiffuse.a;
}
#endif