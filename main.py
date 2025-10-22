import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip
from PIL import Image, ImageTk
import os
import sys

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class TwitchBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PhillipAI")
        self.root.geometry("1400x1000")
        self.root.minsize(1200, 800)
        self.root.configure(bg='#0f0f0f')
        self.root.resizable(True, True)
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TLabel', background='#1a1a1a', foreground='white')
        self.style.configure('TButton', background='#4CAF50', foreground='white')
        self.style.configure('TCombobox', fieldbackground='#2d2d2d', foreground='white')
        
        # Available agents data - organized by character
        self.character_difficulties = {
            'fox': ['medium', 'gm', 'basic', 'auto'],
            'falco': ['medium', 'gm', 'basic', 'auto'],
            'marth': ['medium', 'gm', 'basic', 'auto'],
            'sheik': ['medium', 'gm', 'basic', 'auto'],
            'popo': ['basic', 'auto'],
            'pikachu': ['basic', 'auto'],
            'ganondorf': ['basic', 'auto'],
            'link': ['basic', 'auto'],
            'dk': ['basic', 'auto'],
            'yoshi': ['basic', 'auto'],
            'jigglypuff': ['basic', 'auto'],
            'samus': ['basic', 'auto'],
            'luigi': ['basic', 'auto'],
            'peach': ['basic', 'auto'],
            'cptfalcon': ['basic', 'auto'],
            'doc': ['basic', 'auto']
        }
        
        # All available difficulties
        self.difficulties = ['medium', 'gm', 'basic', 'auto']
        
        # All available characters ordered by Melee tier list
        self.characters = [
            'fox', 'marth', 'jigglypuff', 'falco', 'sheik', 'cptfalcon', 
            'peach', 'popo', 'pikachu', 'yoshi', 'samus', 'luigi', 
            'doc', 'ganondorf', 'dk', 'link'
        ]
        
        self.selected_difficulty = tk.StringVar()
        self.selected_character = tk.StringVar()
        self.generated_command = tk.StringVar()
        self.connect_code = tk.StringVar()
        self.play_command = tk.StringVar()
        
        # Store button references for styling
        self.difficulty_buttons = {}
        self.character_buttons = {}
        
        # Character icon mapping
        self.character_icons = {
            'fox': 'Fox_Standard_CSS Icon_HD.png',
            'marth': 'Marth_Standard_CSS Icon_HD.png',
            'jigglypuff': 'Jigglypuff_Standard_CSS Icon_HD.png',
            'falco': 'Falco_Standard_CSS Icon_HD.png',
            'sheik': 'Sheik_Standard_CSS Icon_HD.png',
            'cptfalcon': 'Cptfalcon_Standard_CSS Icon_HD.png',
            'peach': 'Peach_Standard_CSS Icon_HD.png',
            'popo': 'Popo_Standard_CSS Icon_HD.png',
            'pikachu': 'Pikachu_Standard_CSS Icon_HD.png',
            'yoshi': 'Yoshi_Standard_CSS Icon_HD.png',
            'samus': 'Samus_Standard_CSS Icon_HD.png',
            'luigi': 'Luigi_Standard_CSS Icon_HD.png',
            'doc': 'Doc_Standard_CSS Icon_HD.png',
            'ganondorf': 'Ganondorf_Standard_CSS Icon_HD.png',
            'dk': 'DK_Standard_CSS Icon_HD.png',
            'link': 'Link_Standard_CSS Icon_HD.png'
        }
        
        # Store loaded images
        self.character_images = {}
        self.character_images_selected = {}
        
        self.setup_ui()
        
    def setup_ui(self):
        # Header section with proper sizing
        header_frame = tk.Frame(self.root, bg='#0f0f0f', height=100)
        header_frame.pack(fill='x', pady=(20, 20))
        header_frame.pack_propagate(False)
        
        # Main title with modern styling
        title_label = tk.Label(
            header_frame, 
            text="PhillipAI", 
            font=('Segoe UI', 48, 'bold'),
            bg='#0f0f0f',
            fg='#00bfff'
        )
        title_label.pack(pady=(15, 0))
        
        # Accent line
        accent_line = tk.Frame(header_frame, height=3, bg='#00bfff')
        accent_line.pack(fill='x', padx=300, pady=(10, 0))
        
        # Main container with modern card design
        main_container = tk.Frame(self.root, bg='#0f0f0f')
        main_container.pack(expand=True, fill='both', padx=30, pady=(0, 15))
        
        # Character selection card
        char_card = tk.Frame(main_container, bg='#1a1a1a', relief='flat', bd=0)
        char_card.pack(side='left', fill='both', expand=True, padx=(0, 15))
        
        # Character card header
        char_header = tk.Frame(char_card, bg='#2a2a2a', height=50)
        char_header.pack(fill='x')
        char_header.pack_propagate(False)
        
        tk.Label(
            char_header,
            text="SELECT CHARACTER",
            font=('Segoe UI', 14, 'bold'),
            bg='#2a2a2a',
            fg='#00bfff'
        ).pack(expand=True)
        
        # Character grid with modern styling
        self.character_frame = tk.Frame(char_card, bg='#1a1a1a')
        self.character_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Difficulty selection card
        diff_card = tk.Frame(main_container, bg='#1a1a1a', relief='flat', bd=0, width=300)
        diff_card.pack(side='right', fill='y', padx=(15, 0))
        diff_card.pack_propagate(False)
        
        # Difficulty card header
        diff_header = tk.Frame(diff_card, bg='#2a2a2a', height=50)
        diff_header.pack(fill='x')
        diff_header.pack_propagate(False)
        
        tk.Label(
            diff_header,
            text="SELECT DIFFICULTY",
            font=('Segoe UI', 14, 'bold'),
            bg='#2a2a2a',
            fg='#00bfff'
        ).pack(expand=True)
        
        # Difficulty buttons with modern styling
        self.difficulty_frame = tk.Frame(diff_card, bg='#1a1a1a')
        self.difficulty_frame.pack(fill='x', padx=20, pady=20)
        
        # Modern separator
        separator_frame = tk.Frame(self.root, bg='#0f0f0f', height=20)
        separator_frame.pack(fill='x')
        separator_frame.pack_propagate(False)
        
        separator_line = tk.Frame(separator_frame, height=1, bg='#333333')
        separator_line.pack(fill='x', padx=100, pady=10)
        
        # Instructions section with modern card design
        instructions_card = tk.Frame(self.root, bg='#1a1a1a', relief='flat', bd=0)
        instructions_card.pack(fill='x', padx=30, pady=(0, 20))
        
        # Instructions header
        inst_header = tk.Frame(instructions_card, bg='#2a2a2a', height=50)
        inst_header.pack(fill='x')
        inst_header.pack_propagate(False)
        
        tk.Label(
            inst_header,
            text="SETUP INSTRUCTIONS",
            font=('Segoe UI', 14, 'bold'),
            bg='#2a2a2a',
            fg='#00bfff'
        ).pack(expand=True)
        
        # Instructions content
        instructions_frame = tk.Frame(instructions_card, bg='#1a1a1a')
        instructions_frame.pack(fill='x', padx=30, pady=20)
        
        # Connect Code Section with modern styling
        connect_frame = tk.Frame(instructions_frame, bg='#1a1a1a')
        connect_frame.pack(fill='x', pady=(0, 20))
        
        tk.Label(
            connect_frame,
            text="Enter Your Connect Code:",
            font=('Segoe UI', 16, 'bold'),
            bg='#1a1a1a',
            fg='#ffffff'
        ).pack(anchor='w', pady=(0, 15))
        
        # Modern input field
        input_container = tk.Frame(connect_frame, bg='#2a2a2a', relief='flat', bd=1)
        input_container.pack(fill='x')
        
        self.connect_code_entry = tk.Entry(
            input_container,
            textvariable=self.connect_code,
            font=('Segoe UI', 14),
            bg='#2a2a2a',
            fg='#ffffff',
            relief='flat',
            bd=0,
            insertbackground='#00bfff'
        )
        self.connect_code_entry.pack(fill='x', padx=15, pady=12)
        self.connect_code_entry.bind('<KeyRelease>', self.update_play_command)
        
        # Steps container for horizontal layout
        steps_container = tk.Frame(instructions_frame, bg='#1a1a1a')
        steps_container.pack(fill='x', pady=(0, 10))
        
        # Step 1 Block with modern styling
        step1_frame = tk.Frame(steps_container, bg='#2a2a2a', relief='flat', bd=0)
        step1_frame.pack(side='left', fill='both', expand=True, padx=(0, 15))
        
        # Step 1 header with accent
        step1_header = tk.Frame(step1_frame, bg='#00bfff', height=40)
        step1_header.pack(fill='x')
        step1_header.pack_propagate(False)
        
        tk.Label(
            step1_header,
            text="STEP 1",
            font=('Segoe UI', 12, 'bold'),
            bg='#00bfff',
            fg='#000000'
        ).pack(expand=True)
        
        # Step 1 content
        step1_content = tk.Frame(step1_frame, bg='#2a2a2a')
        step1_content.pack(fill='both', expand=True, padx=15, pady=15)
        
        # Step 1 description
        tk.Label(
            step1_content,
            text="Copy and paste this command\nto x_pilot's Twitch chat:",
            font=('Segoe UI', 11),
            bg='#2a2a2a',
            fg='#cccccc',
            justify='center'
        ).pack(pady=(0, 15))
        
        # Play command display with modern styling
        cmd_container1 = tk.Frame(step1_content, bg='#1a1a1a', relief='flat', bd=1)
        cmd_container1.pack(fill='x', pady=(0, 15))
        
        self.play_command_display = tk.Entry(
            cmd_container1,
            textvariable=self.play_command,
            font=('Segoe UI', 12, 'bold'),
            bg='#1a1a1a',
            fg='#00bfff',
            relief='flat',
            state='readonly',
            justify='center',
            bd=0
        )
        self.play_command_display.pack(fill='x', padx=12, pady=10)
        
        # Modern copy button
        self.copy_play_button = tk.Button(
            step1_content,
            text="COPY PLAY COMMAND",
            command=self.copy_play_command,
            font=('Segoe UI', 10, 'bold'),
            bg='#00bfff',
            fg='#000000',
            relief='flat',
            bd=0,
            padx=20,
            pady=10,
            cursor='hand2',
            activebackground='#0099cc',
            activeforeground='#000000'
        )
        self.copy_play_button.pack(fill='x')
        
        # Step 2 Block with modern styling
        step2_frame = tk.Frame(steps_container, bg='#2a2a2a', relief='flat', bd=0)
        step2_frame.pack(side='left', fill='both', expand=True, padx=(0, 15))
        
        # Step 2 header with accent
        step2_header = tk.Frame(step2_frame, bg='#00bfff', height=40)
        step2_header.pack(fill='x')
        step2_header.pack_propagate(False)
        
        tk.Label(
            step2_header,
            text="STEP 2",
            font=('Segoe UI', 12, 'bold'),
            bg='#00bfff',
            fg='#000000'
        ).pack(expand=True)
        
        # Step 2 content
        step2_content = tk.Frame(step2_frame, bg='#2a2a2a')
        step2_content.pack(fill='both', expand=True, padx=15, pady=15)
        
        # Step 2 description
        tk.Label(
            step2_content,
            text="Copy and paste this command\ninto Twitch chat next:",
            font=('Segoe UI', 11),
            bg='#2a2a2a',
            fg='#cccccc',
            justify='center'
        ).pack(pady=(0, 15))
        
        # Agent command display with modern styling
        cmd_container2 = tk.Frame(step2_content, bg='#1a1a1a', relief='flat', bd=1)
        cmd_container2.pack(fill='x', pady=(0, 15))
        
        self.command_display = tk.Entry(
            cmd_container2,
            textvariable=self.generated_command,
            font=('Segoe UI', 12, 'bold'),
            bg='#1a1a1a',
            fg='#00bfff',
            relief='flat',
            state='readonly',
            justify='center',
            bd=0
        )
        self.command_display.pack(fill='x', padx=12, pady=10)
        
        # Modern copy button
        self.copy_button = tk.Button(
            step2_content,
            text="COPY AGENT COMMAND",
            command=self.copy_command,
            font=('Segoe UI', 10, 'bold'),
            bg='#00bfff',
            fg='#000000',
            relief='flat',
            bd=0,
            padx=20,
            pady=10,
            cursor='hand2',
            activebackground='#0099cc',
            activeforeground='#000000'
        )
        self.copy_button.pack(fill='x')
        
        # Step 3 Block with modern styling
        step3_frame = tk.Frame(steps_container, bg='#2a2a2a', relief='flat', bd=0)
        step3_frame.pack(side='left', fill='both', expand=True)
        
        # Step 3 header with accent
        step3_header = tk.Frame(step3_frame, bg='#00bfff', height=40)
        step3_header.pack(fill='x')
        step3_header.pack_propagate(False)
        
        tk.Label(
            step3_header,
            text="STEP 3",
            font=('Segoe UI', 12, 'bold'),
            bg='#00bfff',
            fg='#000000'
        ).pack(expand=True)
        
        # Step 3 content
        step3_content = tk.Frame(step3_frame, bg='#2a2a2a')
        step3_content.pack(fill='both', expand=True, padx=15, pady=15)
        
        # Step 3 description
        tk.Label(
            step3_content,
            text="In Slippi's direct connect,\nconnect to:",
            font=('Segoe UI', 11),
            bg='#2a2a2a',
            fg='#cccccc',
            justify='center'
        ).pack(pady=(0, 15))
        
        # Slippi connection info with modern styling
        slippi_container = tk.Frame(step3_content, bg='#1a1a1a', relief='flat', bd=1)
        slippi_container.pack(fill='x')
        
        slippi_info = tk.Label(
            slippi_container,
            text="PHAI#591",
            font=('Segoe UI', 18, 'bold'),
            bg='#1a1a1a',
            fg='#FFD700'
        )
        slippi_info.pack(pady=15)
        
        # Load character images
        self.load_character_images()
        
        # Initialize the UI
        self.setup_character_buttons()
        self.setup_difficulty_buttons()
    
    def load_character_images(self):
        """Load and resize character images"""
        icon_size = (64, 64)  # Size for character icons
        
        for character, filename in self.character_icons.items():
            try:
                # Use resource_path to get the correct path for both dev and PyInstaller
                image_path = resource_path(os.path.join("CSS Icons", filename))
                
                if os.path.exists(image_path):
                    # Load and resize image
                    img = Image.open(image_path)
                    # Convert to RGB if necessary (for PNG with transparency)
                    if img.mode in ('RGBA', 'LA'):
                        # Create a white background
                        background = Image.new('RGB', img.size, (255, 255, 255))
                        if img.mode == 'RGBA':
                            background.paste(img, mask=img.split()[-1])  # Use alpha channel as mask
                        else:
                            background.paste(img)
                        img = background
                    elif img.mode != 'RGB':
                        img = img.convert('RGB')
                    
                    img = img.resize(icon_size, Image.Resampling.LANCZOS)
                    
                    # Create PhotoImage for normal state
                    self.character_images[character] = ImageTk.PhotoImage(img)
                    
                    # Create a slightly brighter version for selected state
                    # Add a subtle border effect by creating a slightly larger image with border
                    border_img = Image.new('RGB', (icon_size[0] + 4, icon_size[1] + 4), (255, 255, 255))
                    border_img.paste(img, (2, 2))
                    self.character_images_selected[character] = ImageTk.PhotoImage(border_img)
                    
                else:
                    # Create a placeholder image with character name
                    placeholder = Image.new('RGB', icon_size, (100, 100, 100))
                    self.character_images[character] = ImageTk.PhotoImage(placeholder)
                    self.character_images_selected[character] = ImageTk.PhotoImage(placeholder)
                    
            except Exception as e:
                # Create a placeholder image
                placeholder = Image.new('RGB', icon_size, (100, 100, 100))
                self.character_images[character] = ImageTk.PhotoImage(placeholder)
                self.character_images_selected[character] = ImageTk.PhotoImage(placeholder)
    
    def setup_character_buttons(self):
        """Create all character buttons in a grid"""
        # Clear existing character buttons
        for widget in self.character_frame.winfo_children():
            widget.destroy()
        
        # Create character buttons in a grid
        cols = 4
        for i, character in enumerate(self.characters):
            row = i // cols
            col = i % cols
            
            # Get the image for this character
            image = self.character_images.get(character)
            
            # Create character button with modern styling
            char_button = tk.Button(
                self.character_frame,
                image=image,
                command=lambda c=character: self.select_character(c),
                bg='#2a2a2a',
                relief='flat',
                bd=0,
                cursor='hand2',
                width=70,
                height=70,
                activebackground='#3a3a3a'
            )
            char_button.grid(row=row, column=col, padx=3, pady=3, sticky='ew')
            self.character_buttons[character] = char_button
        
        # Configure grid weights
        for i in range(cols):
            self.character_frame.grid_columnconfigure(i, weight=1)
    
    def setup_difficulty_buttons(self):
        """Create difficulty buttons"""
        # Clear existing difficulty buttons
        for widget in self.difficulty_frame.winfo_children():
            widget.destroy()
        
        # Create difficulty buttons with modern styling
        for i, difficulty in enumerate(self.difficulties):
            diff_button = tk.Button(
                self.difficulty_frame,
                text=difficulty.upper(),
                command=lambda d=difficulty: self.select_difficulty(d),
                font=('Segoe UI', 12, 'bold'),
                bg='#2a2a2a',
                fg='#ffffff',
                relief='flat',
                bd=0,
                padx=15,
                pady=12,
                cursor='hand2',
                width=15,
                activebackground='#3a3a3a',
                activeforeground='#ffffff'
            )
            diff_button.pack(fill='x', pady=5)
            self.difficulty_buttons[difficulty] = diff_button
    
    def select_character(self, character):
        self.selected_character.set(character)
        self.update_difficulty_buttons()
        self.update_command()
        
        # Update character button appearance
        for char, button in self.character_buttons.items():
            if char == character:
                # Use selected image and accent background
                selected_image = self.character_images_selected.get(char)
                button.configure(
                    image=selected_image,
                    bg='#00bfff'
                )
            else:
                # Use normal image and modern gray background
                normal_image = self.character_images.get(char)
                button.configure(
                    image=normal_image,
                    bg='#2a2a2a'
                )
    
    def select_difficulty(self, difficulty):
        self.selected_difficulty.set(difficulty)
        self.update_command()
        
        # Update difficulty button appearance
        for diff, button in self.difficulty_buttons.items():
            if diff == difficulty:
                button.configure(bg='#00bfff', fg='#000000')
            else:
                button.configure(bg='#2a2a2a', fg='#ffffff')
    
    def update_difficulty_buttons(self):
        """Update difficulty buttons based on selected character"""
        character = self.selected_character.get()
        
        if character:
            available_difficulties = self.character_difficulties.get(character, [])
            
            for difficulty, button in self.difficulty_buttons.items():
                if difficulty in available_difficulties:
                    # Enable button
                    button.configure(
                        bg='#2a2a2a',
                        fg='#ffffff',
                        state='normal',
                        cursor='hand2'
                    )
                else:
                    # Disable/gray out button
                    button.configure(
                        bg='#1a1a1a',
                        fg='#666666',
                        state='disabled',
                        cursor='arrow'
                    )
        else:
            # No character selected, disable all difficulty buttons
            for button in self.difficulty_buttons.values():
                button.configure(
                    bg='#1a1a1a',
                    fg='#666666',
                    state='disabled',
                    cursor='arrow'
                )
    
    def update_command(self):
        difficulty = self.selected_difficulty.get()
        character = self.selected_character.get()
        
        if difficulty and character:
            command = f"!agent {difficulty}-{character}"
            self.generated_command.set(command)
        else:
            self.generated_command.set("")
    
    def copy_command(self):
        command = self.generated_command.get()
        if command:
            pyperclip.copy(command)
            messagebox.showinfo("Copied!", f"Command '{command}' copied to clipboard!")
        else:
            messagebox.showwarning("No Command", "Please select both difficulty and character first.")
    
    def update_play_command(self, event=None):
        """Update the play command when connect code changes"""
        connect_code = self.connect_code.get().strip()
        if connect_code:
            play_cmd = f"!play {connect_code}"
            self.play_command.set(play_cmd)
        else:
            self.play_command.set("")
    
    def copy_play_command(self):
        """Copy the play command to clipboard"""
        command = self.play_command.get()
        if command:
            pyperclip.copy(command)
            messagebox.showinfo("Copied!", f"Command '{command}' copied to clipboard!")
        else:
            messagebox.showwarning("No Connect Code", "Please enter your connect code first.")

def main():
    root = tk.Tk()
    app = TwitchBotGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
