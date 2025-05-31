# Node class to represent each song
class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None

# Playlist using Linked List
class MusicPlaylist:
    def __init__(self):
        self.head = None

    def add_song(self, title):
        new_song = SongNode(title)
        if not self.head:
            self.head = new_song
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_song
        print(f"🎶 '{title}' added to playlist.")

    def show_playlist(self):
        if not self.head:
            print("🪫 Playlist is empty.")
            return
        print("🎧 Current Playlist:")
        current = self.head
        while current:
            print(f"➡️ {current.title}")
            current = current.next

    def play_songs(self):
        if not self.head:
            print("🪫 No songs to play.")
            return
        current = self.head
        print("🔊 Playing songs...")
        while current:
            print(f"▶️ Now playing: {current.title}")
            current = current.next

    def remove_song(self, title):
        if not self.head:
            print("🪫 Playlist is empty.")
            return
        if self.head.title == title:
            self.head = self.head.next
            print(f"🗑️ Removed '{title}' from playlist.")
            return
        current = self.head
        while current.next and current.next.title != title:
            current = current.next
        if current.next:
            current.next = current.next.next
            print(f"🗑️ Removed '{title}' from playlist.")
        else:
            print(f"❌ Song '{title}' not found.")
# Create a playlist object
playlist = MusicPlaylist()

# Add songs
playlist.add_song("Habesha Vibes")
playlist.add_song("Yegna Band - Africa")
playlist.add_song("Teddy Afro - Tikur Sew")

# Show all songs
playlist.show_playlist()

# Play songs
playlist.play_songs()

# Remove a song
playlist.remove_song("Yegna Band - Africa")

# Show updated playlist
playlist.show_playlist()

