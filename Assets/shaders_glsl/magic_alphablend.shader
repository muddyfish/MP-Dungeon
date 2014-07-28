//magic_alphablend.shader

varying vec2 Texcoord0;

#ifdef VERTEX_SHADER

uniform mat4 matWorld;
uniform mat4 matView;
uniform mat4 matProj;
uniform vec3 uvOffset;

void main()
{
	vec4 wp = matView * gl_Vertex;
	gl_Position = matProj * wp;

	vec4 uv = gl_Vertex - matWorld * vec4(0.0, 0.0, 0.0, 1.0);
	uv /= uvOffset.x;
	Texcoord0 = 0.5 + uv.xy / 512.0;
}
#endif

#ifdef FRAGMENT_SHADER

uniform sampler2D tex0;
uniform float fade;
uniform vec4 materialDiffuse;

void main()
{
	if(Texcoord0.x < 0.0 || Texcoord0.x > 1.0)
		discard;
	if(Texcoord0.y < 0.0 || Texcoord0.y > 1.0)
		discard;

	gl_FragColor = texture2D(tex0, Texcoord0) * materialDiffuse;
	gl_FragColor.rgb *= fade;
}
#endif
