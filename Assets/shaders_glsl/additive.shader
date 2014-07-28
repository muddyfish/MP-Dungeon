//additive.shader

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
}
#endif

#ifdef FRAGMENT_SHADER

uniform sampler2D tex0;
uniform float fade;
uniform vec4 materialDiffuse;

void main()
{
	gl_FragColor = texture2D(tex0, Texcoord0) * materialDiffuse;
	gl_FragColor.rgb *= fade;
}
#endif
