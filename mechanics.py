# sample mechanics file that I was working on before. Update accordingly to the resolution and FPS. 

extends CharacterBody2D
@onready var animation_player = $AnimationPlayer
@onready var animated_sprite = $AnimatedSprite2D

const SPEED = 300.0
const JUMP_VELOCITY = -400.0

# Get the gravity from the project settings to be synced with RigidBody nodes.
var gravity = ProjectSettings.get_setting("physics/2d/default_gravity")

var current_state

enum state { 
	idle, #0
	walk #1
}
func _ready():
	current_state = state.idle

func _physics_process(delta):
	var direction = Input.get_axis("ui_left", "ui_right")
	if direction:
		velocity.x = direction * SPEED
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)
		
	if direction > 0:
		animated_sprite.flip_h = false
	else:
		animated_sprite.flip_h = true
	
	match current_state:
		state.idle:
			animation_player.play("idle")
			if direction:
				current_state = state.walk
			
		state.walk:
			if not direction:
				current_state= state.idle
				animation_player.play("walk")
		
	
	# Add the gravity.
	if not is_on_floor():
		velocity.y += gravity * delta

	# Handle Jump.
	if Input.is_action_just_pressed("ui_accept") and is_on_floor():
		velocity.y = JUMP_VELOCITY

	# Get the input direction and handle the movement/deceleration.
	# As good practice, you should replace UI actions with custom gameplay actions.
	move_and_slide()
