"""
Properties for Nano Banana Renderer
"""

import bpy
import os
from bpy.types import PropertyGroup
from bpy.props import StringProperty, IntProperty, FloatProperty, BoolProperty, EnumProperty

def get_config_file_path():
    """Get path to config file for storing API key"""
    config_dir = bpy.utils.user_resource('CONFIG')
    if not config_dir:
        config_dir = os.path.expanduser("~/.blender")
    return os.path.join(config_dir, "nano_banana_config.txt")

def save_api_key(api_key):
    """Save API key to config file"""
    try:
        config_path = get_config_file_path()
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        with open(config_path, 'w') as f:
            f.write(api_key)
        return True
    except:
        return False

def load_api_key():
    """Load API key from config file"""
    try:
        config_path = get_config_file_path()
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                return f.read().strip()
    except:
        pass
    return ""

def get_nano_banana_output_dir(context=None):
    """Get NanoBanana output directory relative to current blend file"""
    if bpy.data.filepath:
        blend_dir = os.path.dirname(bpy.data.filepath)
        nano_dir = os.path.join(blend_dir, "NanoBanana")
        os.makedirs(nano_dir, exist_ok=True)
        return nano_dir
    else:
        # Fallback if no blend file is saved
        return os.path.expanduser("~/NanoBanana")

def update_api_key(self, context):
    """Update callback for API key - save it when changed"""
    if self.api_key:
        save_api_key(self.api_key)

class NanoBananaProperties(PropertyGroup):
    # AI Service Selection
    ai_service: EnumProperty(
        name="AI Service",
        description="Choose AI service for processing",
        items=[
            ('ANALYSIS', "Analysis & Advice", "Get professional rendering analysis and suggestions (Gemini)"),
            ('IMAGE_TO_IMAGE', "Image Generation", "Generate new images based on viewport + prompt (Image-to-Image)"),
            ('BOTH', "Analysis + Generation", "Analysis + Image generation"),
        ],
        default='IMAGE_TO_IMAGE'
    )
    
    # API Settings
    api_key: StringProperty(
        name="Gemini API Key",
        description="Your Google Gemini API key",
        default="",
        subtype='PASSWORD',
        update=update_api_key
    )
    
    # Image Prompt for AI Generation
    image_prompt: StringProperty(
        name="Image Prompt",
        description="Describe what you want to generate or transform",
        default="modern architectural building, photorealistic, high quality",
        maxlen=2048
    )
    
    # Image Generation API Settings
    image_gen_service: EnumProperty(
        name="Image Generation Service",
        description="Choose image generation service",
        items=[
            ('REPLICATE', "Replicate API", "Use Replicate for Stable Diffusion (requires API token)"),
            ('HUGGINGFACE', "Hugging Face", "Use Hugging Face Inference API (requires API token)"),
            ('LOCAL', "Local Service", "Use local image generation service"),
        ],
        default='REPLICATE'
    )
    
    image_gen_api_key: StringProperty(
        name="Image Gen API Key",
        description="API key for image generation service (Replicate/HuggingFace)",
        default="",
        subtype='PASSWORD'
    )
    
    # Render Settings
    prompt: StringProperty(
        name="Render Prompt",
        description="Text prompt to guide the AI rendering",
        default="photorealistic render, high quality, detailed",
        maxlen=1024
    )
    
    style_prompt: StringProperty(
        name="Style Prompt",
        description="Additional style guidance for the rendering",
        default="cinematic lighting, professional photography",
        maxlen=512
    )
    
    # Aspect Ratio Settings (Google Gemini 2.5 Flash Image API)
    aspect_ratio: EnumProperty(
        name="Aspect Ratio",
        description="Output image aspect ratio",
        items=[
            ('1:1', "Square (1:1)", "1024x1024 - Perfect for social media posts"),
            ('2:3', "Portrait (2:3)", "832x1248 - Ideal for vertical photography"),
            ('3:2', "Landscape (3:2)", "1248x832 - Classic photography ratio"),
            ('3:4', "Portrait (3:4)", "864x1184 - Standard portrait orientation"),
            ('4:3', "Landscape (4:3)", "1184x864 - Traditional screen ratio"),
            ('4:5', "Portrait (4:5)", "896x1152 - Instagram portrait"),
            ('5:4', "Landscape (5:4)", "1152x896 - Medium format photography"),
            ('9:16', "Vertical (9:16)", "768x1344 - Mobile/story format"),
            ('16:9', "Widescreen (16:9)", "1344x768 - Video/cinematic format"),
            ('21:9', "Ultra-wide (21:9)", "1536x672 - Cinematic ultra-wide"),
        ],
        default='1:1'
    )
    
    # Prompt Enhancement Settings
    prompt_style: EnumProperty(
        name="Prompt Style",
        description="Pre-built prompt templates for different styles",
        items=[
            ('CUSTOM', "Custom", "Use your own prompt"),
            ('PHOTOREALISTIC', "Photorealistic", "Professional photography style"),
            ('ARTISTIC', "Artistic/Stylized", "Stylized illustrations and artwork"),
            ('PRODUCT', "Product Photography", "Commercial product shots"),
            ('MINIMALIST', "Minimalist", "Clean, minimal design"),
            ('COMIC', "Comic/Sequential", "Comic book and storyboard style"),
        ],
        default='CUSTOM'
    )
    
    # Enhanced Prompt Details
    lighting_style: EnumProperty(
        name="Lighting",
        description="Lighting style for the generated image",
        items=[
            ('AUTO', "Auto", "Let AI choose appropriate lighting"),
            ('NATURAL', "Natural", "Natural sunlight or daylight"),
            ('STUDIO', "Studio", "Professional studio lighting setup"),
            ('CINEMATIC', "Cinematic", "Dramatic movie-like lighting"),
            ('GOLDEN_HOUR', "Golden Hour", "Warm, soft sunset/sunrise lighting"),
            ('BLUE_HOUR', "Blue Hour", "Cool, twilight atmosphere"),
            ('LOW_KEY', "Low Key", "Dark, moody lighting with shadows"),
            ('HIGH_KEY', "High Key", "Bright, evenly lit scene"),
        ],
        default='AUTO'
    )
    
    camera_angle: EnumProperty(
        name="Camera Angle",
        description="Camera perspective and angle",
        items=[
            ('AUTO', "Auto", "Let AI choose appropriate angle"),
            ('EYE_LEVEL', "Eye Level", "Standard human perspective"),
            ('LOW_ANGLE', "Low Angle", "Looking up from below"),
            ('HIGH_ANGLE', "High Angle", "Looking down from above"),
            ('BIRDS_EYE', "Bird's Eye", "Top-down aerial view"),
            ('WORMS_EYE', "Worm's Eye", "Extreme low angle upward"),
            ('CLOSE_UP', "Close-up", "Detailed close-up shot"),
            ('WIDE_SHOT', "Wide Shot", "Expansive environmental view"),
        ],
        default='AUTO'
    )
    
    # Image Settings (kept for compatibility but aspect_ratio takes precedence)
    width: IntProperty(
        name="Width",
        description="Render width in pixels",
        default=1024,
        min=256,
        max=2048
    )
    
    height: IntProperty(
        name="Height", 
        description="Render height in pixels",
        default=1024,
        min=256,
        max=2048
    )
    
    # Quality Settings
    quality: EnumProperty(
        name="Quality",
        description="Rendering quality level",
        items=[
            ('LOW', "Low", "Fast rendering, lower quality"),
            ('MEDIUM', "Medium", "Balanced quality and speed"),
            ('HIGH', "High", "Best quality, slower rendering"),
        ],
        default='MEDIUM'
    )
    
    # Advanced Settings
    seed: IntProperty(
        name="Seed",
        description="Random seed for reproducible results (-1 for random)",
        default=-1,
        min=-1,
        max=999999
    )
    
    steps: IntProperty(
        name="Steps",
        description="Number of generation steps",
        default=20,
        min=10,
        max=50
    )
    
    guidance_scale: FloatProperty(
        name="Guidance Scale",
        description="How closely to follow the prompt",
        default=7.5,
        min=1.0,
        max=20.0
    )
    
    # Viewport Settings
    use_viewport_camera: BoolProperty(
        name="Use Viewport Camera",
        description="Use the current viewport camera for rendering",
        default=True
    )
    
    include_scene_context: BoolProperty(
        name="Include Scene Context",
        description="Include scene objects and lighting in the prompt",
        default=True
    )
    
    # UI Settings
    show_advanced: BoolProperty(
        name="Show Advanced",
        description="Show advanced settings",
        default=False
    )