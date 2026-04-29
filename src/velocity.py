import math


def compute_velocity(Re, chord=1.0, nu=1.5e-5):
    return Re * nu / chord


def velocity_components_from_reynolds(Re, alpha_deg, chord=1.0, nu=1.5e-5):
    """Compute (Ux, Uy) from Reynolds number and angle of attack in degrees."""
    U = compute_velocity(Re, chord=chord, nu=nu)
    alpha = math.radians(alpha_deg)
    Ux = U * math.cos(alpha)
    Uy = U * math.sin(alpha)
    return Ux, Uy


def render_u_template(template_text, Re, alpha_deg, chord=1.0, nu=1.5e-5):
    """Replace `internalField uniform (Ux Uy 0);` with computed components."""
    Ux, Uy = velocity_components_from_reynolds(Re, alpha_deg, chord=chord, nu=nu)
    components = f"({Ux:.10g} {Uy:.10g} 0)"
    rendered = template_text.replace("(Ux Uy 0)", components)
    return rendered
