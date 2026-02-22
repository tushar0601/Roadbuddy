/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useState } from "react";
import type { Vehicle } from "@/lib/types";
import { apiJson } from "@/lib/api";
import { toast } from "sonner";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

export function AddVehicleDialog({
  open,
  onOpenChange,
  onCreated,
}: {
  open: boolean;
  onOpenChange: (v: boolean) => void;
  onCreated: (v: Vehicle) => void;
}) {
  const [label, setLabel] = useState("");
  const [plateLast4, setPlateLast4] = useState("");
  const [loading, setLoading] = useState(false);

  async function create() {
    if (!label.trim()) return toast.error("Vehicle label is required");
    if (plateLast4 && plateLast4.length !== 4)
      return toast.error("Plate last4 must be 4 chars");

    setLoading(true);
    try {
      const v = await apiJson<Vehicle>("/vehicles", {
        method: "POST",
        body: JSON.stringify({
          label: label.trim(),
          plate_last4: plateLast4 ? plateLast4.trim() : null,
        }),
      });
      onCreated(v);
      toast.success("Vehicle added");
      setLabel("");
      setPlateLast4("");
      onOpenChange(false);
    } catch (e: any) {
      toast.error(e?.message || "Failed to add vehicle");
    } finally {
      setLoading(false);
    }
  }

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Add new vehicle</DialogTitle>
        </DialogHeader>

        <div className="space-y-4">
          <div className="space-y-2">
            <Label>Label</Label>
            <Input
              value={label}
              onChange={(e) => setLabel(e.target.value)}
              placeholder="Swift / Activa"
            />
          </div>

          <div className="space-y-2">
            <Label>Plate last 4 (optional)</Label>
            <Input
              value={plateLast4}
              onChange={(e) => setPlateLast4(e.target.value)}
              placeholder="1234"
              maxLength={4}
            />
          </div>

          <Button onClick={create} disabled={loading}>
            {loading ? "Saving..." : "Create vehicle"}
          </Button>
        </div>
      </DialogContent>
    </Dialog>
  );
}
