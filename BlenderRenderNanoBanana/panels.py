"""
UI Panels for Nano Banana Renderer
"""

import bpy
from bpy.types import Panel

class NANOBANANA_PT_render_panel(Panel):
    """Main panel for Nano Banana Renderer"""
    bl_label = "Nano Banana Renderer"
    bl_idname = "NANOBANANA_PT_render_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    bl_category = "Nano Banana"
    
    def draw(self, context):
        layout = self.layout
        props = context.scene.nano_banana
        
        # API Setup Section
        box = layout.box()
        box.label(text="Gemini 2.5 Flash Image API", icon='KEYFRAME_HLT')
        
        if not props.api_key:
            # No API key set - show setup button
            col = box.column()
            col.alert = True
            col.label(text="API Key Required", icon='ERROR')
            col.operator("nano_banana.api_key_dialog", text="Setup API Key", icon='KEY_HLT')
        else:
            # API key is set - show masked key and test button
            row = box.row()
            masked_key = props.api_key[:8] + "..." + props.api_key[-4:] if len(props.api_key) > 12 else "***"
            row.label(text=f"Key: {masked_key}", icon='LOCKED')
            
            row = box.row()
            row.operator("nano_banana.api_key_dialog", text="Change Key", icon='KEY_HLT')
            row.operator("nano_banana.setup_api", text="Test Connection", icon='LINKED')
        
        # Render Settings Section
        box = layout.box()
        box.label(text="AI Service Settings", icon='RENDER_STILL')
        
        col = box.column()
        col.prop(props, "ai_service", text="Service")
        
        # Show different options based on service selection
        if props.ai_service == 'ANALYSIS':
            col.label(text="✓ Professional rendering analysis", icon='INFO')
        elif props.ai_service == 'IMAGE_TO_IMAGE':
            col.label(text="✓ Generate new images from viewport", icon='IMAGE_DATA')
        elif props.ai_service == 'BOTH':
            col.label(text="✓ Analysis + image generation", icon='SEQUENCE')
        
        # 统一使用image_prompt作为主提示词
        col.prop(props, "image_prompt", text="Main Prompt")
        col.prop(props, "style_prompt", text="Style")
        
        # Aspect Ratio Setting
        col.separator()
        col.prop(props, "aspect_ratio", text="Aspect Ratio")
        
        # Prompt Enhancement
        col.separator()
        col.label(text="Prompt Enhancement:", icon='MODIFIER')
        col.prop(props, "prompt_style", text="Style Template")
        
        row = col.row()
        row.prop(props, "lighting_style", text="Lighting")
        row.prop(props, "camera_angle", text="Camera")
        
        row = box.row()
        row.prop(props, "quality", text="Quality")
        
        # Advanced Settings (collapsible)
        box = layout.box()
        row = box.row()
        row.prop(props, "show_advanced", text="Advanced Settings", 
                icon='TRIA_DOWN' if props.show_advanced else 'TRIA_RIGHT',
                emboss=False)
        
        if getattr(props, 'show_advanced', False):
            col = box.column()
            col.prop(props, "seed", text="Seed")
            col.prop(props, "steps", text="Steps")
            col.prop(props, "guidance_scale", text="Guidance Scale")
            
            col.separator()
            col.prop(props, "use_viewport_camera", text="Use Viewport Camera")
            col.prop(props, "include_scene_context", text="Include Scene Context")
        
        # ================================
        # MAIN RENDER BUTTON - ALWAYS VISIBLE
        # ================================
        layout.separator()
        layout.separator()
        
        # 创建主要的渲染按钮区域
        render_box = layout.box()
        render_box.label(text="🍌 NanoBanana AI Render", icon='RENDER_STILL')
        
        # 获取当前服务类型
        current_service = getattr(props, 'ai_service', 'IMAGE_TO_IMAGE')
        print(f"Panel显示 - 当前服务: {current_service}")
        
        # 根据服务类型设置按钮文本
        if current_service == 'ANALYSIS':
            button_text = "🔍 Analyze Scene"
            button_icon = 'VIEWZOOM'
        elif current_service == 'IMAGE_TO_IMAGE':
            button_text = "🎨 Generate Image from Viewport"
            button_icon = 'IMAGE_DATA'
        elif current_service == 'BOTH':
            button_text = "🚀 Analysis + Generation"
            button_icon = 'SEQUENCE'
        else:
            button_text = "🍌 Start AI Render"
            button_icon = 'RENDER_STILL'
        
        print(f"Panel显示 - 按钮文本: {button_text}")
        
        # 创建大按钮
        col = render_box.column(align=True)
        col.scale_y = 2.0
        
        # 主渲染按钮 - 强制显示
        col.operator("nano_banana.render_viewport_fixed", text=button_text, icon=button_icon)
        
        # 服务信息
        render_box.separator()
        info_col = render_box.column(align=True)
        
        if current_service == 'IMAGE_TO_IMAGE':
            info_col.label(text="• Capture current viewport", icon='CAMERA_DATA')
            info_col.label(text="• Generate AI enhanced image", icon='IMAGE_DATA')
            info_col.label(text="• Save to project folder", icon='FILE_IMAGE')
        elif current_service == 'ANALYSIS':
            info_col.label(text="• Analyze scene composition", icon='VIEWZOOM')
            info_col.label(text="• Get improvement suggestions", icon='FILE_TEXT')
        elif current_service == 'BOTH':
            info_col.label(text="• Complete AI workflow", icon='SEQUENCE')
            info_col.label(text="• Analysis + Image generation", icon='RENDER_STILL')
        
        # Prompt输入
        layout.separator()
        prompt_box = layout.box()
        prompt_box.label(text="AI Prompt", icon='GREASEPENCIL')
        prompt_box.prop(props, "image_prompt", text="")
        
        # Quick settings for 3D Viewport
        settings_row = prompt_box.row()
        settings_row.prop(props, "aspect_ratio", text="")
        settings_row.prop(props, "prompt_style", text="")
        
        # 状态显示
        if hasattr(context.scene, 'nano_banana_status'):
            layout.separator()
            status_box = layout.box()
            status_box.label(text="Status", icon='INFO')
            status_box.label(text=context.scene.nano_banana_status)


class NANOBANANA_PT_viewport_panel(Panel):
    """3D Viewport panel for quick AI rendering"""
    bl_label = "🍌 AI Render"
    bl_idname = "NANOBANANA_PT_viewport_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "NanoBanana"
    
    def draw(self, context):
        layout = self.layout
        props = context.scene.nano_banana
        
        # 检查API密钥
        if not props.api_key:
            layout.label(text="⚠️ Setup API Key First", icon='ERROR')
            layout.operator("nano_banana.setup_api", text="Setup API Key", icon='PREFERENCES')
            return
        
        # 快速服务选择
        layout.prop(props, "ai_service", text="")
        
        # 获取当前服务类型
        current_service = getattr(props, 'ai_service', 'IMAGE_TO_IMAGE')
        
        # 根据服务类型设置按钮
        if current_service == 'ANALYSIS':
            button_text = "🔍 Analyze Scene"
            button_icon = 'VIEWZOOM'
        elif current_service == 'IMAGE_TO_IMAGE':
            button_text = "🎨 Generate Image"
            button_icon = 'IMAGE_DATA'
        elif current_service == 'BOTH':
            button_text = "🚀 Analysis + Generation"
            button_icon = 'SEQUENCE'
        else:
            button_text = "🍌 AI Render"
            button_icon = 'RENDER_STILL'
        
        # 主要渲染按钮
        layout.separator()
        col = layout.column(align=True)
        col.scale_y = 2.0
        col.operator("nano_banana.render_viewport_fixed", text=button_text, icon=button_icon)
        
        # 简化的信息
        layout.separator()
        box = layout.box()
        box.scale_y = 0.8
        
        if current_service == 'IMAGE_TO_IMAGE':
            box.label(text="• Viewport → AI Image", icon='IMAGE_DATA')
        elif current_service == 'ANALYSIS':
            box.label(text="• Scene Analysis", icon='VIEWZOOM')
        elif current_service == 'BOTH':
            box.label(text="• Complete Workflow", icon='SEQUENCE')
        
        # 快速提示词输入
        layout.separator()
        layout.prop(props, "image_prompt", text="", icon='GREASEPENCIL')


class NANOBANANA_PT_sidebar_panel(Panel):
    """Sidebar panel for Layout workspace"""
    bl_label = "🍌 NanoBanana AI"
    bl_idname = "NANOBANANA_PT_sidebar_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"
    
    def draw(self, context):
        layout = self.layout
        props = context.scene.nano_banana
        
        # API状态指示
        if props.api_key:
            row = layout.row(align=True)
            row.label(text="🔑 API Ready", icon='LINKED')
            row.operator("nano_banana.setup_api", text="", icon='PREFERENCES')
        else:
            layout.label(text="⚠️ No API Key", icon='ERROR')
            layout.operator("nano_banana.setup_api", text="Setup API", icon='PREFERENCES')
            return
        
        layout.separator()
        
        # 服务选择
        layout.prop(props, "ai_service")
        
        # 获取当前服务
        current_service = getattr(props, 'ai_service', 'IMAGE_TO_IMAGE')
        
        # 主按钮
        layout.separator()
        if current_service == 'IMAGE_TO_IMAGE':
            layout.operator("nano_banana.render_viewport_fixed", 
                          text="🎨 Generate AI Image", 
                          icon='IMAGE_DATA')
            
            # 功能说明
            box = layout.box()
            box.label(text="Will capture current view", icon='CAMERA_DATA')
            box.label(text="and generate AI image", icon='IMAGE_DATA')
            
        elif current_service == 'ANALYSIS':
            layout.operator("nano_banana.render_viewport_fixed", 
                          text="🔍 Analyze Scene", 
                          icon='VIEWZOOM')
            
            box = layout.box()
            box.label(text="AI will analyze your", icon='VIEWZOOM')
            box.label(text="scene and give advice", icon='FILE_TEXT')
            
        elif current_service == 'BOTH':
            layout.operator("nano_banana.render_viewport_fixed", 
                          text="🚀 Complete AI Workflow", 
                          icon='SEQUENCE')
            
            box = layout.box()
            box.label(text="Analysis + Image", icon='SEQUENCE')
            box.label(text="generation together", icon='RENDER_STILL')
        
        # 提示词
        layout.separator()
        layout.label(text="Prompt:", icon='GREASEPENCIL')
        layout.prop(props, "image_prompt", text="")
        
        # 快速设置
        layout.separator()
        layout.label(text="Quick Settings:", icon='PREFERENCES')
        
        # Aspect ratio and style in compact layout
        row = layout.row()
        row.prop(props, "aspect_ratio", text="")
        row.prop(props, "prompt_style", text="")
        
        layout.operator("nano_banana.test_connection", text="Test API", icon='NETWORK_DRIVE')