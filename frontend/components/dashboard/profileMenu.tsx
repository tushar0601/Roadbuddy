"use client";

import { useRouter } from "next/navigation";
import { supabase } from "@/lib/supabaseClient";
import { useAuth } from "@/lib/auth";
import { useSupabaseUser } from "@/hooks/useSupabaseUser";

import { Button } from "@/components/ui/button";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { toast } from "sonner";

function initialsFromEmail(email: string) {
  const name = email.split("@")[0] || "U";
  return name.slice(0, 2).toUpperCase();
}

export function ProfileMenu() {
  const router = useRouter();
  const { setToken } = useAuth();
  const { email } = useSupabaseUser();

  async function logout() {
    try {
      await supabase.auth.signOut();
    } catch {
    } finally {
      setToken(null);
      toast.success("Logged out");
      router.replace("/signin");
    }
  }

  const display = email ?? "Account";
  const fallback = email ? initialsFromEmail(email) : "U";

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="outline" className="gap-2">
          <Avatar className="h-6 w-6">
            <AvatarFallback>{fallback}</AvatarFallback>
          </Avatar>
          <span className="hidden sm:inline">{display}</span>
        </Button>
      </DropdownMenuTrigger>

      <DropdownMenuContent align="end" className="w-64">
        <DropdownMenuLabel>Profile</DropdownMenuLabel>
        <div className="px-2 pb-2 text-sm text-muted-foreground break-all">
          {email ?? "Signed in"}
        </div>

        <DropdownMenuSeparator />

        <DropdownMenuItem onClick={logout} className="cursor-pointer">
          Log out
        </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  );
}
