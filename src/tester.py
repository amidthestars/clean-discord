from helper import extract_fields

message="choderoki	Name: gabby\nAge: 15\nGender: female\nSexuality: bi \nStatus: single\nPronouns: she/her\nLikes: gaming, chatting vcs, caffeine, music, anime, shiney things, youtube.\nDislikes: body shaming.\nLocation: u.s. Oklahoma central time\nDms: always open\nStyle: nu goth/punk\nHmu if you find me interesting\nYou have to come to me:"
print("\n".join(extract_fields(message)))