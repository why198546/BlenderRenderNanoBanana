# 📦 Releases

## [v1.37] - 2025-11-03 (Image Display Enhancement)

### 🖼️ Improved Image Popup Display
**Download**: [BlenderRenderNanoBanana_v1.37.zip](BlenderRenderNanoBanana_v1.37.zip) (28.6 KB)

- **Added**: Large, centered popup window for generated images
- **Added**: Automatic image size calculation (max 800x600, maintains aspect ratio)
- **Added**: Enhanced popup UI with image information display
- **Added**: Direct save and view buttons in popup window
- **Improved**: Better image preview experience with emoji icons
- **UI**: Smart window sizing based on image dimensions

**New Image Display Features**:
- 🎨 Large centered popup showing full AI-generated image
- 📐 Automatic sizing with aspect ratio preservation
- 💾 Direct save button in popup window
- 👁️ One-click view in Image Editor
- 📊 Image dimension information display
- 🎯 Improved user experience for viewing results

---

## [v1.36] - 2025-11-03 (UI Enhancement)

### 🎨 Layout Workspace Panel Enhancement
**Download**: [BlenderRenderNanoBanana_v1.36.zip](BlenderRenderNanoBanana_v1.36.zip)

- **Added**: Aspect ratio selection to Layout workspace panel
- **Added**: Prompt enhancement options (style templates) to Layout workspace panel
- **Added**: Lighting and camera angle controls for image generation
- **Improved**: Better compact layout for advanced AI controls
- **UI**: Now all workspaces have consistent AI enhancement options

**New Layout Panel Features**:
- 🎭 Aspect Ratio dropdown (1:1 to 21:9 formats)
- 🎨 Prompt Style Templates (Photorealistic, Artistic, Product, etc.)
- 💡 Lighting Style controls (Natural, Studio, Cinematic, etc.)
- 📷 Camera Angle options (Eye Level, Low Angle, Bird's Eye, etc.)

---

## [v1.35] - 2025-11-03 (Hotfix)

### 🔧 Critical Bug Fix
**Download**: [BlenderRenderNanoBanana_v1.35.zip](BlenderRenderNanoBanana_v1.35.zip)

- **Fixed**: `base64_data` variable name error that prevented AI image generation
- **Issue**: API requests were failing due to undefined variable reference
- **Solution**: Corrected variable name from `base64_data` to `image_data`

**This is a critical hotfix - please update immediately if using v1.34**

---

## [v1.34] - 2025-11-03

### 🍌 Blender Render Nano Banana v1.34 - AI Image Generation with Aspect Ratios

**Download**: [BlenderRenderNanoBanana_v1.34.zip](BlenderRenderNanoBanana_v1.34.zip)

### ✨ Major Features
- **Google Gemini 2.5 Flash Image API integration** - Latest AI image generation technology
- **10 aspect ratios support** (1:1 to 21:9 ultra-wide) - Perfect for any output format
- **Professional prompt enhancement system** - AI-powered prompt optimization
- **Multi-workspace UI** (Properties/Viewport/Sidebar) - Access from anywhere in Blender
- **Auto F12-like display experience** - Generated images automatically appear
- **Version-controlled file saves** (.001, .002, etc.) - Never lose your work

### 🎨 New AI Features
- **Smart lighting control** (8 styles) - Natural, Studio, Cinematic, Golden Hour, Blue Hour, Low Key, High Key
- **Camera angle options** (8 perspectives) - Eye Level, Low Angle, High Angle, Bird's Eye, Worm's Eye, Close-up, Wide Shot
- **Prompt templates** (Photorealistic, Artistic, Product, Minimalist, Comic) - Professional results with one click
- **Enhanced prompt building** with technical details - Automatic lighting and camera descriptions
- **Quality levels** (Low/Medium/High) - Balance speed vs quality

### 🔧 Technical Improvements
- **Unified prompt system** across all panels - Consistent experience everywhere
- **Aspect ratio API integration** - Native Google Gemini 2.5 Flash support
- **Smart file management** in project folders - Organized output structure
- **Comprehensive error handling** - Better debugging and user feedback

### 📋 Requirements
- **Blender**: 4.5 or newer
- **Python**: 3.10+ (included with Blender)
- **Internet**: Required for API communication
- **API Key**: Google Gemini API key ([Get yours here](https://aistudio.google.com/apikey))

### 🎯 Perfect For
- Architectural visualization
- Product design and rendering
- Creative AI art generation
- Concept art and ideation
- Social media content creation

---

## Installation Instructions

1. **Download** the latest release zip file
2. **Open Blender** → Edit → Preferences → Add-ons
3. **Click "Install..."** and select the downloaded zip file
4. **Enable** "Render: Nano Banana Renderer"
5. **Get your API key** from [Google AI Studio](https://aistudio.google.com/apikey)
6. **Setup** in Properties → Render → Nano Banana Renderer → "Setup API Key"

## Support

- 📖 [Full Documentation](../README.md)
- 🐛 [Report Issues](https://github.com/why198546/BlenderRenderNanoBanana/issues)
- 💡 [Feature Requests](https://github.com/why198546/BlenderRenderNanoBanana/discussions)

---

*Made with ❤️ for the Blender community*