//terrain.shader

varying vec4 UV;	// xy: territoryType; zw: tiles

#ifdef VERTEX_SHADER

uniform mat4 matWorld;
uniform mat4 matView;
uniform mat4 matProj;

void main()
{
	gl_Position = matProj * matView * matWorld * gl_Vertex;
	UV.xy = gl_MultiTexCoord0.xy;
	UV.zw = gl_MultiTexCoord0.xy * vec2(8.0, 4.0);	// multiply by (8.0, 4.0) to match the 2048x1024 texture size
}
#endif

#ifdef FRAGMENT_SHADER

uniform sampler2D tex0;	// tile 0 (Background)
uniform sampler2D tex1;	// tile 1
uniform sampler2D tex2;	// tile 2
uniform sampler2D tex3;	// tile 3
uniform sampler2D tex4;	// map of the terrain type

uniform float fade;
uniform vec4 materialDiffuse;

void main()
{
	vec3 terrainType = texture2D(tex4, UV.xy).rgb;

	gl_FragColor.a = 1.0;
	gl_FragColor = texture2D(tex0, UV.zw);											// Tile 0 (Background)
	gl_FragColor = mix(gl_FragColor, texture2D(tex1, UV.zw), terrainType.r);		// Tile 1
	gl_FragColor = mix(gl_FragColor, texture2D(tex2, UV.zw), terrainType.g);		// Tile 2
	gl_FragColor = mix(gl_FragColor, texture2D(tex3, UV.zw), terrainType.b);		// Tile 3

	gl_FragColor *= materialDiffuse;
	gl_FragColor.rgb *= fade;
}
#endif
