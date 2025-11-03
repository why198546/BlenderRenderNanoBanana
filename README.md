# 🍌 Blender Render Nano Banana

> A powerful Blender addon that integrates Google Gemini 2.5 Flash Image API for AI-powered viewport rendering and image generation.

![Blender Version](https://img.shields.io/badge/Blender-4.5%2B-orange)
![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![API](https://img.shields.io/badge/API-Google%20Gemini%202.5%20Flash-red)

## ✨ Features

### 🎯 Core Functionality
- **AI Viewport Rendering**: Transform your 3D viewport into stunning AI-generated images
- **Multi-Workspace UI**: Access from Properties panel, 3D Viewport tabs, and sidebar
- **Automatic F12-like Experience**: Generated images automatically display in image editor
- **Smart File Management**: Version-controlled saves (`.001`, `.002`, etc.) in project directories

### 🎨 Advanced AI Features
- **Google Gemini 2.5 Flash Image Integration**: Latest AI image generation technology
- **10 Aspect Ratios**: From square (1:1) to ultra-wide (21:9) cinematic formats
- **Professional Prompt Templates**: Photorealistic, artistic, product photography, minimalist, comic styles
- **Smart Lighting Control**: 8 lighting styles including golden hour, studio, cinematic
- **Camera Angle Options**: Eye-level, low-angle, bird's eye, close-up, and more
- **Quality Levels**: Low, medium, and high-quality generation options

### 🔧 Technical Capabilities
- **Scene Context Analysis**: Optional inclusion of scene objects and lighting data
- **Enhanced Prompt Building**: Automatic technical detail injection
- **Base64 Image Processing**: Efficient viewport capture and API communication
- **Error Handling**: Comprehensive error reporting and debugging features

## 🚀 Quick Start

### Installation

1. **Download the latest release** from the [Releases page](../../releases)
2. **Install in Blender**:
   - Open Blender → Edit → Preferences → Add-ons
   - Click "Install..." and select the downloaded `.zip` file
   - Enable "Render: Nano Banana Renderer"

### Setup

1. **Get your Gemini API key** from [Google AI Studio](https://aistudio.google.com/apikey)
2. **Configure the addon**:
   - Go to Properties → Render → Nano Banana Renderer
   - Click "Setup API Key" and enter your key
   - Test the connection

### Usage

#### Method 1: Properties Panel
1. Navigate to **Properties → Render → Nano Banana Renderer**
2. Enter your prompt in "Main Prompt"
3. Choose aspect ratio and style options
4. Click "🍌 Generate AI Image"

#### Method 2: 3D Viewport (Quick Access)
1. In 3D Viewport, go to **NanoBanana** tab
2. Enter prompt and adjust quick settings
3. Click "🚀 AI Generate from Viewport"

#### Method 3: Sidebar (Minimal)
1. Press `N` to open sidebar, go to **Tool** tab
2. Find "🍌 NanoBanana AI" panel
3. Enter prompt and generate

## 🎛️ Interface Locations

| Location | Access | Features |
|----------|---------|----------|
| **Properties Panel** | Properties → Render | Full control panel with all settings |
| **3D Viewport Tab** | 3D Viewport → NanoBanana | Quick generation with essential controls |
| **Sidebar Panel** | 3D Viewport → N → Tool | Minimal interface for fast workflow |

## 🎨 Aspect Ratios Supported

| Ratio | Resolution | Best For |
|-------|------------|----------|
| 1:1 | 1024×1024 | Social media posts |
| 2:3 | 832×1248 | Vertical photography |
| 3:2 | 1248×832 | Classic photography |
| 3:4 | 864×1184 | Standard portraits |
| 4:3 | 1184×864 | Traditional screens |
| 4:5 | 896×1152 | Instagram portraits |
| 5:4 | 1152×896 | Medium format |
| 9:16 | 768×1344 | Mobile/stories |
| 16:9 | 1344×768 | Video/cinematic |
| 21:9 | 1536×672 | Ultra-wide cinematic |

## 💡 Prompt Templates

### Photorealistic
Perfect for architectural visualization and product renders:
```
"A photorealistic scene of [your content], captured with professional camera equipment, emphasizing natural lighting and fine details"
```

### Artistic/Stylized
Great for creative interpretations:
```
"A stylized artistic illustration of [your content], featuring creative interpretation and enhanced visual appeal"
```

### Product Photography
Ideal for commercial presentations:
```
"A high-resolution, studio-lit product photograph of [your content], with clean background and professional lighting setup"
```

## 🔧 Requirements

- **Blender**: 4.5 or newer
- **Python**: 3.10+ (included with Blender)
- **Internet**: Required for API communication
- **API Key**: Google Gemini API key (free tier available)

## 📁 File Organization

Generated images are automatically saved to:
```
[Your .blend file directory]/NanoBanana/
├── Generated_Image_20241103_143022.png
├── Generated_Image_20241103_143022.001.png
├── Generated_Image_20241103_143022.002.png
└── ...
```

## 🛠️ Development

### Version History

- **v1.34** - Aspect ratio support, prompt enhancement system
- **v1.33** - Unified prompt system, version control for files
- **v1.32** - Multi-workspace support, automatic F12-like display
- **v1.31** - Basic AI image generation integration
- **v1.0** - Initial release

### Building from Source

```bash
git clone https://github.com/[username]/BlenderRenderNanoBanana.git
cd BlenderRenderNanoBanana
zip -r BlenderRenderNanoBanana.zip BlenderRenderNanoBanana/
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [Google Gemini API Documentation](https://ai.google.dev/gemini-api/docs/image-generation)
- [Get Gemini API Key](https://aistudio.google.com/apikey)
- [Blender API Documentation](https://docs.blender.org/api/current/)

## ⚠️ Disclaimer

This addon requires an active internet connection and a Google Gemini API key. API usage may incur costs based on Google's pricing. Please review Google's terms of service and pricing before use.

---

**Made with ❤️ for the Blender community**