//window.shader

struct INTERP_DATA
{
#ifdef VERTEX_SHADER
	float4 Pos : POSITION;
#endif
	float2 UV : TEXCOORD0;
};

#ifdef VERTEX_SHADER

float4x4 matScreenAligned;
float2 texelOffset;

struct VS_INPUT
{
	float4 Pos : POSITION;
	float2 Texcoord0 : TEXCOORD0;
};

INTERP_DATA main(VS_INPUT In)
{
	INTERP_DATA Out = (INTERP_DATA)0;
	Out.Pos = mul(In.Pos, matScreenAligned);
	Out.Pos.xy += texelOffset * Out.Pos.ww;
	Out.UV = In.Texcoord0;
	return Out;
}
#endif

#ifdef PIXEL_SHADER

sampler2D tex0;
float fade;

struct PS_OUTPUT
{
	float4 Color : COLOR;
};

PS_OUTPUT main(INTERP_DATA In)
{
	PS_OUTPUT Out = (PS_OUTPUT)0;
	Out.Color = tex2D(tex0, In.UV);
	Out.Color.rgb *= fade;
	return Out;
}
#endif
