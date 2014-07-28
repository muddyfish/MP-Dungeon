//water.shader

varying float UV_y;

#ifdef VERTEX_SHADER

uniform mat4 matWorld;
uniform mat4 matView;
uniform mat4 matProj;

void main()
{
	gl_Position = matProj * matView * matWorld * gl_Vertex;
	UV_y = gl_MultiTexCoord0.y;
}
#endif

#ifdef FRAGMENT_SHADER

uniform sampler2D tex0;
uniform float fade;
uniform vec4 materialDiffuse;

void main()
{
	gl_FragColor = texture2D(tex0, vec2(0.0, UV_y)) * materialDiffuse;
	gl_FragColor.rgb *= fade;
}
#endif
