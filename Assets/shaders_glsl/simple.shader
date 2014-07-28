//simple.shader

#ifdef VERTEX_SHADER

uniform mat4 matWorld;
uniform mat4 matView;
uniform mat4 matProj;

void main()
{
	vec4 wPos = matWorld * gl_Vertex;
	vec4 wp = matView * wPos;
	gl_Position = matProj * wp;
}
#endif

#ifdef FRAGMENT_SHADER

uniform float visibility;
uniform float fade;
uniform vec4 materialDiffuse;

void main()
{
	gl_FragColor = materialDiffuse;
	gl_FragColor.a *= visibility;
	gl_FragColor.rgb *= fade;
}
#endif
